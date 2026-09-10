# batuta

The conductor's baton. This repository holds Henok's workflow for agents inside Maestri: the skillset, the terminal roles, the scripts and the templates. It is project-agnostic.

## Layout

- `skillset/` — the Nori skillset `personal/batuta`: the global CLAUDE.md (`AGENTS.md`), the skills (Nori's execution core plus Matt Pocock's definition skills) and the subagents. Linked into Nori with `nori-skillsets link`.
- `roles/` — the three Maestri roles. The preset in the app is only a pointer; the truth lives here.
  - `definer.md` — the front door. Everything Henok brings enters here: ideas, defects, small asks with no open decision, findings after a round closed, tickets other people opened that he wants worked, and the order of the next round. Grills, writes glossary and ADRs, publishes specs and defined tickets to Linear, applies `ready-for-agent` (only the Definer ever applies it), and writes the manifest in the `round` note with Henok, in the order Henok gives. Never chooses the order itself, never starts a round.
  - `orchestrator.md` — runs one round: the tickets on the manifest, in that order, and nothing else. Writes the slice plan, recruits executors, verifies against spec and tests. Inside the concurrency limit: at most two slices in flight, three only when the third belongs to a ticket that already has one. From Henok it hears only "go", "close the round", "emergency", and his answers to the lines it wrote in `for you`; anything else gets one line back: take it to the Definer. Never edits a repository.
  - `executor.md` — one plan, one worktree, TDD with manual falsification, a PR for Henok to merge. Restarted once its PR is verified green.
- `bin/` — scripts:
  - `setup-canvas` — creates and wires the five standing notes and installs the routines. Rerun it in the Orchestrator terminal after any change to a routine prompt or to the `how it works` template: it recreates what is missing and refreshes those; the other notes hold live content and are never overwritten.
  - `notify-maestri.sh` — Claude Code Notification hook that opens Maestri on click instead of Terminal.
  - `speak`, `listen`, `grill-voice` — the voice kit: local text-to-speech (Kokoro), local speech-to-text (whisper.cpp), and a terminal that speaks a frontier of questions, records each answer while Space is held, transcribes it, and sends everything back to the agent. Adapted from João's "Grelha por Voz".
- `templates/` — initial content of the canvas notes and the preset text.
- `docs/workflow.md` — how a round runs, from the manifest to Henok's merge and the state note.
- `docs/adr/` — the decisions that shaped the workflow. Read them before changing a role.
- `CONTEXT.md` — the glossary of the workflow itself: round, manifest, slice, finding, concurrency limit.
- `test/` — `bash test/setup-canvas-test.sh`.
- `archive/notes/` — the notes from the old workspaces, exported on 2026-09-08, to be mined for ADRs and glossary entries.

## How the work splits

Definition before dispatch, one round at a time. Henok brings everything to the Definer: ideas, defects, small asks with no open decision, findings after a round closed, tickets other people opened that he wants worked, and the order of the next round. The Definer defines, publishes the tickets, applies `ready-for-agent` (nobody else ever does), and writes the manifest with Henok: at most three tickets, in the order Henok gives. It never chooses the order itself and never starts a round. Nothing else enters the flow, and nobody audits a backlog.

With the manifest in the `round` note, Henok says "go" to the Orchestrator, which dispatches only those tickets, in that order, inside the concurrency limit: at most two slices in flight, three only when the third belongs to a ticket that already has one. It writes plans whose Testing Plan is untouchable and recruits executors with a model and effort chosen per ticket. The executor grills only implementation decisions, waits instead of assuming, and delivers a PR assigned to Henok, with evidence. Verification is against the spec, not only against the tests. Henok merges every PR himself. What turns up along the way is a finding: one line in the `findings` note, never a ticket, a label, a plan change or a dispatch in the round it appeared, however urgent. The exception is a production emergency, one of four measured facts: one "Emergency:" line in `for you`, and Henok decides whether to open an emergency round. The round closes with the `state · <date>` note, and after it the Orchestrator dispatches nothing until Henok types `/clear`.

Details in `docs/workflow.md` and in the roles.

## Installing on a new machine

```
git clone git@github.com:henokteixeira/batuta.git ~/Documents/programming/batuta
nori-skillsets link ~/Documents/programming/batuta/skillset --name batuta
nori-skillsets switch personal/batuta
ln -sf ~/Documents/programming/batuta/bin/{speak,listen,grill-voice} ~/bin/
```

Then, in Maestri, create the three roles with the text in `templates/presets.md`. With the roles in place, run `bin/setup-canvas` in the Orchestrator terminal, with Maestro Mode on: it creates and wires the five standing notes and installs the routines. Point the Notification hook in `~/.claude/settings.json` to `bin/notify-maestri.sh`. The voice kit needs `brew install ffmpeg whisper-cpp`, the whisper model in `~/.cache/whisper-cpp/ggml-large-v3-turbo.bin`, and a Kokoro venv in `~/Library/Application Support/batuta-tts/` (see `docs/workflow.md`).
