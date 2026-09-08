"""grill-voice — answer a grilling round by voice, one question at a time.

Usage: grill-voice <agent> [--lang pt|en|auto] [--speak pt|en] [--file path]
Reads ~/.cache/grill/<agent>.txt: blocks separated by a blank line; the first line of a
block is its label (Q1…). Speaks the question (Kokoro via `speak`), records the answer while
Space is held, transcribes (whisper.cpp), shows it, and finally sends everything to the agent
with `maestri ask`.
"""
import argparse, os, signal, subprocess, sys, tempfile, time, shutil
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.rule import Rule
import readchar

C = Console(highlight=False)
MODEL = os.environ.get("LISTEN_MODEL", str(Path.home() / ".cache/whisper-cpp/ggml-large-v3-turbo.bin"))
DEVICE = os.environ.get("LISTEN_DEVICE", ":1")
PROMPT = os.environ.get("LISTEN_PROMPT", "Pergunta um, opção A. Pergunta dois, opção B.")

KEYS = [("⏎", "send"), ("e", "edit"), ("r", "re-record (hold space)"), ("o", "hear the question"), ("a", "hear your answer"),
        ("t", "type"), ("+", "append by voice"), ("s", "skip"), ("q", "quit without sending")]

_player = None


def play(path, block=True):
    global _player
    stop_play()
    _player = subprocess.Popen(["afplay", path])
    if block:
        try:
            _player.wait()
        except KeyboardInterrupt:
            stop_play()


def stop_play():
    global _player
    if _player and _player.poll() is None:
        _player.terminate()
    _player = None


def speak(text, lang):
    env = dict(os.environ, SPEAK_NO_PLAY="1")
    with C.status("[dim]synthesizing…[/]", spinner="dots"):
        r = subprocess.run(["speak", text, lang], env=env, capture_output=True, text=True)
    path = r.stdout.strip()
    if path and os.path.exists(path):
        play(path, block=False)
        return path
    return None


def _raw_stdin():
    import termios, tty
    fd = sys.stdin.fileno(); old = termios.tcgetattr(fd); tty.setcbreak(fd)
    return fd, old


def _restore_stdin(fd, old):
    import termios
    termios.tcsetattr(fd, termios.TCSADRAIN, old)


def wait_playback():
    import select
    if not (_player and _player.poll() is None):
        return
    fd, old = _raw_stdin()
    try:
        with Live(Text.assemble((" 🔈 ", ""), ("speaking the question… ", "cyan"), ("⏎ or space to skip", "dim")),
                  refresh_per_second=4, console=C, transient=True):
            while _player and _player.poll() is None:
                r, _, _ = select.select([sys.stdin], [], [], 0.1)
                if r:
                    os.read(fd, 64); stop_play(); break
    finally:
        import termios; termios.tcflush(fd, termios.TCIFLUSH); _restore_stdin(fd, old)
    time.sleep(0.25)


def record(q_audio=None):
    import select, termios
    HOLD_GAP = float(os.environ.get("LISTEN_HOLD_GAP", "0.7"))
    wav = tempfile.mktemp(suffix=".wav", prefix="grill-")
    fd, old = _raw_stdin()
    ff = None; t0 = None
    try:
        with Live(refresh_per_second=10, console=C, transient=True) as live:
            live.update(Text.assemble((" ⎵ ", "bold cyan"), ("hold SPACE to talk", "cyan"),
                                      ("   ·   ", "dim"), ("[o]", "bold cyan"), (" hear the question again", "dim"),
                                      ("   ·   ", "dim"), ("[⏎]", "bold cyan"), (" type", "dim"),
                                      ("   ·   ", "dim"), ("[q]", "bold cyan"), (" quit", "dim")))
            while True:
                r, _, _ = select.select([sys.stdin], [], [], 0.2)
                if not r: continue
                ch = os.read(fd, 1)
                if ch == b" ": stop_play(); break
                if ch in (b"o", b"O") and q_audio: play(q_audio, block=False)
                if ch in (b"\r", b"\n"): stop_play(); return "TYPE"
                if ch in (b"q", b"Q", b"\x03"): stop_play(); return "QUIT"
            ff = subprocess.Popen(
                ["ffmpeg", "-hide_banner", "-loglevel", "error", "-f", "avfoundation", "-i", DEVICE,
                 "-ac", "1", "-ar", "16000", "-t", "300", wav],
                stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            t0 = time.time(); last = t0
            while True:
                dot = "●" if int((time.time() - t0) * 2) % 2 == 0 else "○"
                live.update(Text.assemble((f" {dot} ", "bold red"), ("recording ", "red"),
                                          (f"{time.time()-t0:4.0f}s", "dim"), ("   release to stop", "dim")))
                r, _, _ = select.select([sys.stdin], [], [], 0.05)
                if r:
                    ch = os.read(fd, 1)
                    if ch == b" ": last = time.time(); continue
                    if ch in (b"\r", b"\n"): break
                if time.time() - last > HOLD_GAP: break
            time.sleep(0.15)
    finally:
        if ff:
            ff.send_signal(signal.SIGINT)
            try: ff.wait(timeout=5)
            except subprocess.TimeoutExpired: ff.kill()
        termios.tcflush(fd, termios.TCIFLUSH)
        _restore_stdin(fd, old)
    if t0 and time.time() - t0 < 0.4:
        return None
    if not os.path.exists(wav) or os.path.getsize(wav) < 2000:
        return None
    vd = subprocess.run(["ffmpeg", "-hide_banner", "-i", wav, "-af", "volumedetect", "-f", "null", "-"],
                        capture_output=True, text=True).stderr
    for line in vd.splitlines():
        if "mean_volume:" in line:
            try:
                if float(line.split("mean_volume:")[1].split("dB")[0]) < -45:
                    return None
            except ValueError:
                pass
    return wav


def transcribe(wav, lang):
    with C.status("[dim]transcribing…[/]", spinner="dots"):
        r = subprocess.run(["whisper-cli", "-m", MODEL, "-l", lang, "-f", wav, "-nt", "-np",
                            "--prompt", PROMPT, "-nth", "0.5"], capture_output=True, text=True)
    return " ".join(l.strip() for l in r.stdout.splitlines() if l.strip())


def load_questions(path):
    blocks, cur = [], []
    for line in Path(path).read_text().splitlines() + [""]:
        if line.strip():
            cur.append(line.rstrip())
        elif cur:
            blocks.append((cur[0].strip(), "\n".join(cur[1:]).strip()))
            cur = []
    return blocks


def edit_text(initial):
    try:
        import readline
        readline.set_startup_hook(lambda: readline.insert_text(initial))
        try:
            return input("  › ").strip()
        finally:
            readline.set_startup_hook()
    except Exception:
        f = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False); f.write(initial); f.close()
        subprocess.call([os.environ.get("EDITOR", "nano"), f.name])
        return Path(f.name).read_text().strip()


def help_line():
    t = Text()
    for i, (k, d) in enumerate(KEYS):
        if i: t.append("  ·  ", "dim")
        t.append(f"[{k}]", "bold cyan"); t.append(f" {d}", "dim")
    return t


def show_answer(answer):
    C.print(Panel(Text(answer or "(empty)", style="bold"), title="[green]your answer[/]", border_style="green", padding=(0, 2)))


def ask_one(idx, total, label, body, lang, speak_lang):
    C.print()
    C.print(Panel(body, title=f"[bold]{label}[/]  [dim]{idx}/{total}[/]", border_style="cyan", padding=(1, 2)))
    q_audio = speak(body, speak_lang)
    answer, a_audio = None, None
    need_record = True
    append = False
    while True:
        if need_record:
            wait_playback()
            wav = record(q_audio)
            stop_play()
            if wav == "QUIT":
                C.print("\n[dim]leaving without sending.[/]"); sys.exit(1)
            if wav == "TYPE":
                answer = C.input("  [cyan]›[/] ").strip() or answer
                need_record = False
                show_answer(answer)
                C.print(help_line()); k = readchar.readkey()
                if k in (readchar.key.ENTER, "\r", "\n") and answer: return answer
                need_record = k in ("r", "R"); continue
            if wav is None:
                C.print("  [yellow]nothing captured[/] [dim](tap too short or silent take — hold space while you talk)[/]")
                continue
            text = transcribe(wav, lang)
            answer = f"{answer} {text}".strip() if (answer and a_audio and append) else text
            a_audio = wav
            append = False
            need_record = False
            show_answer(answer)
        C.print(help_line())
        k = readchar.readkey()
        if k in (readchar.key.ENTER, "\r", "\n"):
            if answer: return answer
            C.print("  [yellow]empty answer — record or type[/]"); need_record = True
        elif k in ("r", "R"):
            need_record = True
        elif k in ("o", "O"):
            if q_audio: play(q_audio, block=False)
        elif k in ("a", "A"):
            if a_audio: play(a_audio, block=False)
        elif k in ("e", "E"):
            stop_play()
            answer = edit_text(answer or "") or answer
            show_answer(answer)
        elif k in ("t", "T"):
            stop_play()
            answer = C.input("  [cyan]›[/] ").strip() or answer
            show_answer(answer)
        elif k == "+":
            append = True; need_record = True
        elif k in ("s", "S"):
            return "(skipped)"
        elif k in ("q", "Q", readchar.key.CTRL_C):
            stop_play(); C.print("\n[dim]leaving without sending.[/]"); sys.exit(1)


def help_line_send():
    t = Text(); t.append("[⏎]", "bold cyan"); t.append(" send everything   ", "dim")
    t.append("[q]", "bold cyan"); t.append(" cancel", "dim"); return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("--lang", default=os.environ.get("LISTEN_LANG", "auto"), help="language you speak: auto|pt|en")
    ap.add_argument("--speak", default=os.environ.get("GRILL_SPEAK_LANG", "pt"), help="language the questions are spoken in: pt|en")
    ap.add_argument("--file")
    a = ap.parse_args()
    path = a.file or Path.home() / f".cache/grill/{a.agent}.txt"
    if not Path(path).exists():
        C.print(f"[red]no questions at {path}[/]"); sys.exit(1)
    for tool in ("ffmpeg", "whisper-cli", "speak", "maestri"):
        if not shutil.which(tool):
            C.print(f"[red]{tool} is not on PATH[/]"); sys.exit(1)
    qs = load_questions(path)
    w0 = shutil.get_terminal_size().columns; t0 = time.time()
    while time.time() - t0 < 1.5 and shutil.get_terminal_size().columns == w0 == 80:
        time.sleep(0.1)
    C.print(Rule(f"[bold]grill-voice[/] · {a.agent} · {len(qs)} questions", style="cyan"))
    answers = []
    for i, (label, body) in enumerate(qs, 1):
        answers.append((label, ask_one(i, len(qs), label, body, a.lang, a.speak)))

    C.print(); C.print(Rule("[bold]summary[/]", style="green"))
    tb = Table(show_header=False, box=None, padding=(0, 1))
    for label, ans in answers:
        tb.add_row(f"[bold cyan]{label}[/]", ans)
    C.print(tb); C.print()
    C.print(help_line_send())
    k = readchar.readkey()
    if k not in (readchar.key.ENTER, "\r", "\n"):
        C.print("[dim]not sent.[/]"); sys.exit(1)
    msg = "\n".join(f"{l}: {t}" for l, t in answers)
    body = ("Spoken answers from Henok (transcribed with local whisper; if anything reads as nonsense "
            "or needs detail, ask back instead of assuming):\n" + msg)
    with C.status(f"[dim]sending to {a.agent}…[/]", spinner="dots"):
        r = subprocess.run(["maestri", "ask", a.agent, body], capture_output=True, text=True)
    ok = r.returncode == 0
    C.print(f"[{'green' if ok else 'red'}]{'sent' if ok else 'failed'}[/] → {a.agent}")
    if not ok: C.print(Text(r.stderr.strip()[-400:], style="dim"))
    speak("Sent." if ok else "Sending failed.", a.speak)
    time.sleep(1.2); stop_play()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stop_play(); C.print("\n[dim]interrupted.[/]"); sys.exit(130)
