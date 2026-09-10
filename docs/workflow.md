# How the Batuta workflow runs

Written on 2026-09-08, the night the workflow was assembled. Read this before opening the canvas.

## In one sentence

Define before dispatching: you and the Definer close the business rule and the decisions in batches and write the manifest of the next round, at most three tickets in order; the Orchestrator runs only that manifest through disposable executors and stops at verified PRs; you merge every one of them; nobody assumes, everybody asks and waits.

## The canvas

One workspace for Shema, called **Shema**, rooted at `~/Documents/programming/obt`. In it:

- **Definidor** (the Definer) — the terminal you talk to, and the front door. Everything you want enters here: ideas, defects, small asks with no open decision, findings after a round closed, tickets other people opened that you want worked, and the order of the next round. It defines, and it writes the manifest with you. Fable, effort `max`: `claude --effort max`.
- **Orquestrador** (the Orchestrator) — the terminal that runs the round: only the tickets on the manifest, in that order. From you it hears "go", "close the round", "emergency", and your answers to the lines it wrote in `for you`. Fable, effort `max`, never lower: `claude --effort max`. Needs **Maestro Mode on** to recruit executors: toggle it on the terminal the first time.
- **voice** — a Shell terminal for the voice kit, wired to the Definer. `bin/setup-canvas`, run in the Orchestrator terminal with Maestro Mode on, creates it, creates and wires the five standing notes, and schedules the three routines. A missing standing note is fixed by rerunning `setup-canvas`, never by creating it by hand.
- Five standing notes with fixed names: **round** (the manifest; outside a round its body reads `(no round open)`), **board** (one line per slice of the open round, in manifest order: `<codename> · <ticket> · <state> · <model>`; emptied at round close), **for you** (only what is still pending on you), **findings** (what showed up out of scope, one line each), and **how it works** (the short version of this file). The **logs** stack holds `log · <codename>`, `state · <date>` and `definition · <date>`; you almost never open it.
- Three routines: **morning state** daily at 08:30, **evening round check** daily at 18:30, **for you reminder** on weekdays at noon. They read the round note and the latest state note, report on the board, clean `for you` of what you already answered, and push you the reminder; the evening check also closes the round, but only when every manifest item is merged or waiting Henok. A routine never opens a round and never closes one by the clock.

The old workspaces are in the **Arquivo** folder inside the Shema YWAM group, intact, with their terminals and notes. Delete them whenever you like; the notes are exported in `batuta/archive/notes/`. The **teste** workspace in "Arquivo (apagar)" was the mould and can be deleted. **Quick Sermon** was not touched.

## A round, start to finish

1. **Define.** Open the Definer and bring everything: ideas, defects seen in a test, small asks, `Define:` lines the Orchestrator left in `for you`, the findings it marked at the last round close, and tickets other people opened that you want worked. Only what you bring here enters the flow; nobody audits a backlog. It grills item by item, one frontier per question round, each question with the recommended answer. Facts it finds itself; only decisions come to you. It updates the glossary (`CONTEXT.md`) and writes ADRs as it goes, publishes spec and tickets to Linear with blockers, and labels `ready-for-agent` only what is whole: rule in one sentence, acceptance criterion as a failing test, zero open decisions. Only the Definer ever applies that label, and every ticket it labels, with either label, is assigned to you. A small ask with no open decision is closed in one exchange, without a grilling session. A definition session can run while a round is in flight; what it defines waits for the next manifest and never joins the running round.
2. **Manifest.** The Definer writes the round note with you: a first line `round · <date>`, then at most three tickets in the order they run, one per line — `1. ENG-905 (leaf)`, `2. ENG-894 (parent, 4 leaves)`. A parent counts as one item; its unblocked children are its slices. You give the order; the Definer never chooses it and never starts a round.
3. **go.** Type `/clear` in the Orchestrator and say "go". It reads the latest `state · <date>` note, finishes any post-merge bookkeeping the previous round left, then reads the manifest and dispatches only those tickets, in that order: not other `ready-for-agent` tickets, not findings, not urgent items, not anything you mention in passing. For each slice it writes the plan in `~/.maestri/handoff/<branch>/plan.md` with the untouchable Testing Plan and the enumerated paths, creates the worktree, recruits an executor with the ticket's model and effort, and dispatches. At most two slices in flight, three only when the third belongs to a ticket that already has one: that is the concurrency limit. One slice grilling you at a time. A manifest ticket it cannot dispatch, because of a blocker outside the manifest or a missing label, gets a `Define:` line in `for you` and is skipped; it resumes in the same round once the Definer has labelled it, and the Orchestrator never pulls the blocker in. If the round note says `(no round open)`, it tells you there is no manifest and waits.
4. **Answer.** You only look at `for you`. Every item is one plain `- ` bullet, still pending on you: a closed question with its recommended answer, `Approve:`, `Define:`, `Look:`, `Review and merge PR #N`, `Run:` for a wizard script, or an emergency. Each line says what is needed, why, and what it unblocks. A design question is never a question here: it comes as a `Define:` line. You answer by appending `R: …` to the line, or by voice. Nothing is ever ticked: the agent that wrote the line deletes it once your answer or your merge is recorded on the ticket, and you may delete a line yourself once you did it. Measurements, history and status go to `log · <codename>` or the state note, never here.
5. **Verify.** The executor delivers a PR with evidence: suite pasted, falsification of every test, what it did outside the plan. The Orchestrator reads the diff, runs everything, runs the reviewer on both axes (standards and faithfulness to the spec), waits for CI, and only then writes `Review and merge PR #N` in `for you` and restarts the executor. Every PR an agent opens is assigned to you, and you merge every one yourself; no agent merges. The item is then waiting Henok, which frees its slot, and the Orchestrator learns of the merge with `gh pr view <N> --json state,mergedAt`. If you request changes with the round open, it re-dispatches from the plan on disk to a fresh executor; with the round closed, the state note records `not merged: PR #N, changes requested` and the ticket goes back to the Definer. A PR you close without merging: your reason on the ticket, ticket back to the Definer. Visible changes you check in the portal or simulator.
6. **Close.** The round closes when every manifest item is merged or waiting Henok, or when you say "close the round". The Orchestrator records the decisions on the tickets, marks each finding line `⇒ candidate` or `⇒ recommend discard` and deletes none, writes `state · <date>` in the logs stack (merged, waiting your merge, blocked and why, measured, not finished, and the manifest itself), empties the board, sets the round note back to `(no round open)`, and ends with TASK_COMPLETE if every item was merged, else BLOCKED: waiting on Henok. If you close with a slice still working: from reviewing onwards it finishes to a verified PR and is recorded as waiting Henok; before that it stops, its executor is restarted, its plan and worktree stay on disk, the state note says `not finished: <ticket>, plan at <path>`, and the ticket goes back to the Definer for the next manifest. A stopped slice never resumes by itself. After the state note the Orchestrator only answers questions and does post-merge bookkeeping; it dispatches nothing, however small and whoever asks, until you type `/clear`.

The next round starts with a new manifest written with the Definer, then `/clear` in the Orchestrator and "go". The notes are the memory; the session is not.

## Mid-round asks and emergencies

Anything you bring to the Orchestrator that is not "go", "close the round", "emergency" or an answer to one of its own `for you` lines gets a one-line answer: take it to the Definer. The Definer answers questions about the running round from `board`, `for you`, `round` and the latest state note; it never `maestri ask`s the Orchestrator and never relays a request to it. The only thing that reaches the Orchestrator from a definition session is the round note. A finding is one line in `findings` and nothing more in the round it appeared: never a ticket, never a label, never a plan change, never a dispatch, however urgent. Only the Definer, in a session with you, turns a marked line into a ticket or discards it, and deletes the line then; findings about other people's tickets or the wider backlog are discarded. A production emergency is one of four measured facts, never a judgement: production is down or returning errors to users; production data is being lost or corrupted; a secret or personal data is exposed; money is being spent or charged wrongly. Anything else that looks urgent is a finding. On an emergency the Orchestrator, or an executor through it, writes one line in `for you` — `Emergency: <the measured fact, one sentence>. Open an emergency round? Recommend <yes|no>.` — and does nothing else: no ticket, no label, no fix, no remount, no dispatch. You decide. If yes, the Definer defines the ticket in one exchange and appends `emergency: <ticket>` to the round note, or writes a one-item manifest if no round is open; you say "emergency" to the Orchestrator, which dispatches that slice next, ahead of the manifest order and inside the concurrency limit. It closes with the round.

## High-autonomy round

Only when you ask. The Definer closes everything you brought and writes the whole frontier into the round note, with `mode: high autonomy` under the date. For that round only, the three-ticket cap and the concurrency limit are suspended and the Orchestrator fires the manifest at once with `maestri ask --batch`. The mode line lives in the round note, never on the board; at close the note goes back to `(no round open)`. Never the default.

## Models

Decisions and study on the strongest: Definer and Orchestrator on Fable with effort `max`, never lower. Implementation on the cheapest the ticket allows: estimate 1 or 2 and low risk, sonnet with low effort; 3, sonnet with high effort; 5, high risk or domain rule, opus with high effort. Faithfulness reviewer on opus. Never haiku.

## The voice kit

Three scripts in `batuta/bin`, symlinked into `~/bin`, everything local:

- `speak "text" [pt|en]` — Kokoro text-to-speech (falls back to macOS `say`). Audio is cached per text.
- `listen [pt|en|auto]` — records from the microphone until Enter and transcribes with whisper.cpp large-v3-turbo. Silent takes are rejected instead of hallucinated.
- `grill-voice <agent>` — reads `~/.cache/grill/<agent>.txt` (one block per question, first line is the label), speaks each question, records your answer while you hold Space, transcribes, lets you confirm, edit, re-record or type, and finally sends all answers to the agent in one `maestri ask`.

How a voice session goes: the Definer writes the spoken version of its frontier to `~/.cache/grill/Definidor.txt` and tells you to run `grill-voice Definidor`. You run it in the **voice** Shell terminal, which is wired to the Definer. Answer in whole sentences ("option A, because…"), not single words: whisper transcribes sentences better. Keys before recording: hold Space to talk, `o` hears the question again, Enter types instead, `q` quits. With a transcription on screen: Enter accepts, `r` re-records, `+` appends, `e` edits, `t` types, `a` plays your take, `s` skips.

Requirements, already installed: `ffmpeg`, `whisper-cpp` (Homebrew), the model at `~/.cache/whisper-cpp/ggml-large-v3-turbo.bin`, and the Kokoro venv with models at `~/Library/Application Support/batuta-tts/`. The microphone is device `:1` (MacBook Pro Microphone); change with `LISTEN_DEVICE`. The one thing only you can do: give Maestri microphone permission in System Settings › Privacy & Security › Microphone, the first time `listen` or `grill-voice` records.

## Where everything lives

- `~/Documents/programming/batuta` — this repository: skillset, roles, scripts, templates. Private on GitHub at `henokteixeira/batuta`.
- `~/.claude/CLAUDE.md` — generated by Nori from `batuta/skillset/AGENTS.md`. Active skillset: `personal/batuta`.
- Roles in Maestri (`Definidor`, `Orquestrador`, `Executor`) — only pointers to `batuta/roles/*.md`. Edit the file, not the preset.
- Linear, team Engineering — labels `ready-for-agent` and `ready-for-human`; only the Definer ever applies `ready-for-agent`, and every ticket it labels, with either label, is assigned to you. Tickets other people open there enter the flow only when you bring them to the Definer; nothing in Linear is listed, audited or dispatched because it is sitting there.

## What changed in Nori

Skillset `personal/batuta` instead of `public/high-autonomy`. Out: brainstorming, root-cause-tracing, creating-debug-tests-and-iterating, webapp-testing, building-ui-ux, ui-ux-experimentation, creating-a-skillset, updating-noridocs and the documentation and pattern subagents. In: grilling, grill-me, grill-with-docs, domain-modeling, to-spec, to-tickets, code-review, handoff, wizard, to-questionnaire and wayfinder. The six Maestri skills and the Mac cleanup skill are now part of the skillset so a switch cannot delete them.

## Notification

The Claude Code Notification hook points to `batuta/bin/notify-maestri.sh`: inside Maestri, clicking the notification opens Maestri; outside it, it falls back to Nori's hook.

## After editing the workflow

- `skillset/AGENTS.md`: run `nori-skillsets switch personal/batuta` and redo the four checks below.
- A role file in `batuta/roles/`: type `/clear` in that terminal. The preset re-reads the file at the next session.
- A note template or a routine prompt: rerun `bin/setup-canvas` in the Orchestrator terminal. It recreates any missing standing note, refreshes `how it works` from its template and refreshes the routine prompts; `board`, `for you`, `findings` and `round` hold live content and are never overwritten, so a change to their templates reaches only a new workspace.

## After any `nori-skillsets switch`

The switch reinstalls `settings.json` and deletes from `~/.claude/skills` whatever is not in the skillset. Check and redo:

1. Notification hook pointing to `batuta/bin/notify-maestri.sh`.
2. Nori's PreToolUse hook `commit-author.js` removed (it swaps the co-author for Nori).
3. `includeCoAuthoredBy: true`, so the co-author is Claude.
4. Never override the git author: the global config is `henokteixeira <henokteixeira@gmail.com>`, which is the GitHub account; `gh` and the Linear MCP are logged in as Henok too, so `--assignee @me` on GitHub and assignee `me` on Linear are him.
