# How the Batuta workflow runs

Written on 2026-09-08, the night the workflow was assembled. Read this before opening the canvas.

## In one sentence

Define before dispatching: you and the Definer close the business rule and the decisions in batches; the Orchestrator only receives ready tickets and takes them to verified PRs through disposable executors; nobody assumes, everybody asks and waits.

## The canvas

One workspace for Shema, called **Shema**, rooted at `~/Documents/programming/obt`. In it:

- **Definidor** (the Definer) — the terminal you talk to in order to define. Fable, high effort.
- **Orquestrador** (the Orchestrator) — the terminal that runs the queue. Fable, high effort while planning. Needs **Maestro Mode on** to recruit executors: toggle it on the terminal the first time.
- **voice** — a Shell terminal for the voice kit, wired to the Definer (create it once: New Terminal → Shell → connect it to Definidor).
- Four notes: **board** (one line per task in flight), **for you** (only what is blocked on you; closed questions), **findings** (what showed up out of scope; only grows), and the **logs** stack (the state of each round and the log of each task; you almost never open it).

The old workspaces are in the **Arquivo** folder inside the Shema YWAM group, intact, with their terminals and notes. Delete them whenever you like; the notes are exported in `batuta/archive/notes/`. The **teste** workspace in "Arquivo (apagar)" was the mould and can be deleted. **Quick Sermon** was not touched.

## A round, start to finish

1. **Define.** Open the Definer and bring the list: tickets, defects seen in a test, ideas, `Define:` lines the Orchestrator left in `for you`. It works for tickets already in Linear and for things that are not tickets yet. It grills item by item, one frontier per round, each question with the recommended answer. Facts it finds itself; only decisions come to you. It updates the glossary (`CONTEXT.md`) and writes ADRs as it goes, publishes spec and tickets to Linear with blockers, and labels `ready-for-agent` only what is whole: rule in one sentence, acceptance criterion as a failing test, zero open decisions.
2. **Dispatch.** Tell the Orchestrator to start the round. It lists the `ready-for-agent` tickets with no blocker, writes the slice plan in `~/.maestri/handoff/<branch>/plan.md` with the untouchable Testing Plan and the enumerated paths, creates the worktree, recruits an executor with the ticket's model and effort, and dispatches. At most three tasks in flight and one grilling you at a time.
3. **Answer.** You only look at `for you`. Each line is a closed question or a high-risk approval. Answer there, by voice (Whispr Flow, or the voice kit below). When you answer, the line goes away.
4. **Verify.** The executor delivers a PR with evidence: suite pasted, falsification of every test, what it did outside the plan. The Orchestrator reads the diff, runs everything, runs the reviewer on both axes (standards and faithfulness to the spec), waits for CI, and only then advances the board. Visible changes you check in the portal or simulator.
5. **Close.** Decisions go as a comment on the ticket. Findings become tickets or are discarded. The executor is restarted. At the end the Orchestrator writes `state · <date>` in the logs stack and ends with TASK_COMPLETE or BLOCKED.

The next round starts in a restarted Orchestrator reading that note. The notes are the memory; the session is not.

## High-autonomy mode

Only when you ask. The Definer closes the whole queue first; when nothing is left to define, it writes `mode: high autonomy` as the first line of the board. The Orchestrator then fires the whole frontier at once, without the limit of three. When it closes the round, it deletes the line. Never the default.

## Models

Decisions and study on the strongest: Definer and Orchestrator on Fable, high effort. Implementation on the cheapest the ticket allows: estimate 1 or 2 and low risk, sonnet with low effort; 3, sonnet with high effort; 5, high risk or domain rule, opus with high effort. Faithfulness reviewer on opus. Never haiku.

## The voice kit

Three scripts in `batuta/bin`, symlinked into `~/bin`, everything local:

- `speak "text" [pt|en]` — Kokoro text-to-speech (falls back to macOS `say`). Audio is cached per text.
- `listen [pt|en|auto]` — records from the microphone until Enter and transcribes with whisper.cpp large-v3-turbo. Silent takes are rejected instead of hallucinated.
- `grill-voice <agent>` — reads `~/.cache/grill/<agent>.txt` (one block per question, first line is the label), speaks each question, records your answer while you hold Space, transcribes, lets you confirm, edit, re-record or type, and finally sends all answers to the agent in one `maestri ask`.

How a voice round goes: the Definer writes the spoken version of its frontier to `~/.cache/grill/Definidor.txt` and tells you to run `grill-voice Definidor`. You run it in the **voice** Shell terminal, which is wired to the Definer. Answer in whole sentences ("option A, because…"), not single words: whisper transcribes sentences better. Keys before recording: hold Space to talk, `o` hears the question again, Enter types instead, `q` quits. With a transcription on screen: Enter accepts, `r` re-records, `+` appends, `e` edits, `t` types, `a` plays your take, `s` skips.

Requirements, already installed: `ffmpeg`, `whisper-cpp` (Homebrew), the model at `~/.cache/whisper-cpp/ggml-large-v3-turbo.bin`, and the Kokoro venv with models at `~/Library/Application Support/batuta-tts/`. The microphone is device `:1` (MacBook Pro Microphone); change with `LISTEN_DEVICE`. The one thing only you can do: give Maestri microphone permission in System Settings › Privacy & Security › Microphone, the first time `listen` or `grill-voice` records.

## Where everything lives

- `~/Documents/programming/batuta` — this repository: skillset, roles, scripts, templates. Private on GitHub at `henokteixeira/batuta`.
- `~/.claude/CLAUDE.md` — generated by Nori from `batuta/skillset/AGENTS.md`. Active skillset: `personal/batuta`.
- Roles in Maestri (`Definidor`, `Orquestrador`, `Executor`) — only pointers to `batuta/roles/*.md`. Edit the file, not the preset.
- Linear, team Engineering — labels `ready-for-agent` and `ready-for-human`. Six documentation-cleanup tickets, one per repository, already created (ENG-837 to ENG-842).
- `CONTEXT.md` for internalization-room (PR #131) and shema-api (PR #342) — waiting for your review.

## What changed in Nori

Skillset `personal/batuta` instead of `public/high-autonomy`. Out: brainstorming, root-cause-tracing, creating-debug-tests-and-iterating, webapp-testing, building-ui-ux, ui-ux-experimentation, creating-a-skillset, updating-noridocs and the documentation and pattern subagents. In: grilling, grill-me, grill-with-docs, domain-modeling, to-spec, to-tickets, code-review, handoff, wizard, to-questionnaire and wayfinder. The six Maestri skills and the Mac cleanup skill are now part of the skillset so a switch cannot delete them.

## Notification

The Claude Code Notification hook points to `batuta/bin/notify-maestri.sh`: inside Maestri, clicking the notification opens Maestri; outside it, it falls back to Nori's hook.

## After any `nori-skillsets switch`

The switch reinstalls `settings.json` and deletes from `~/.claude/skills` whatever is not in the skillset. Check and redo:

1. Notification hook pointing to `batuta/bin/notify-maestri.sh`.
2. Nori's PreToolUse hook `commit-author.js` removed (it swaps the co-author for Nori).
3. `includeCoAuthoredBy: true`, so the co-author is Claude.
4. Never override the git author: the global config is `henokteixeira <henokteixeira@gmail.com>`, which is the GitHub account.
