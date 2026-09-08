# batuta

The conductor's baton. This repository holds Henok's workflow for agents inside Maestri: the skillset, the terminal roles, the scripts and the templates. It is project-agnostic.

## Layout

- `skillset/` — the Nori skillset `personal/batuta`: the global CLAUDE.md (`AGENTS.md`), the skills (Nori's execution core plus Matt Pocock's definition skills) and the subagents. Linked into Nori with `nori-skillsets link`.
- `roles/` — the three Maestri roles. The preset in the app is only a pointer; the truth lives here.
  - `definer.md` — talks to Henok, grills, writes glossary and ADRs, publishes specs and defined tickets to Linear.
  - `orchestrator.md` — pulls `ready-for-agent` tickets, writes the slice plan, recruits executors, verifies against spec and tests. Never edits a repository.
  - `executor.md` — one plan, one worktree, TDD with manual falsification, a PR. Dies with the PR.
- `bin/` — scripts:
  - `notify-maestri.sh` — Claude Code Notification hook that opens Maestri on click instead of Terminal.
  - `speak`, `listen`, `grill-voice` — the voice kit: local text-to-speech (Kokoro), local speech-to-text (whisper.cpp), and a terminal that speaks a grilling round, records each answer while Space is held, transcribes it, and sends everything back to the agent. Adapted from João's "Grelha por Voz".
- `templates/` — initial content of the canvas notes and the preset text.
- `docs/workflow.md` — how the workflow runs, from ticket to merge.
- `archive/notes/` — the notes from the old workspaces, exported on 2026-09-08, to be mined for ADRs and glossary entries.

## How the work splits

Definition before dispatch. The Definer closes business rules, acceptance criteria and decisions with Henok, in batches. The Orchestrator only receives tickets labelled `ready-for-agent`, slices them into plans whose Testing Plan is untouchable, and dispatches executors with a model and effort chosen per ticket. The executor grills only implementation decisions, waits instead of assuming, and delivers a PR with evidence. Verification is against the spec, not only against the tests.

Details in `docs/workflow.md` and in the roles.

## Installing on a new machine

```
git clone git@github.com:henokteixeira/batuta.git ~/Documents/programming/batuta
nori-skillsets link ~/Documents/programming/batuta/skillset --name batuta
nori-skillsets switch personal/batuta
ln -sf ~/Documents/programming/batuta/bin/{speak,listen,grill-voice} ~/bin/
```

Then, in Maestri, create the three roles with the text in `templates/presets.md`, and point the Notification hook in `~/.claude/settings.json` to `bin/notify-maestri.sh`. The voice kit needs `brew install ffmpeg whisper-cpp`, the whisper model in `~/.cache/whisper-cpp/ggml-large-v3-turbo.bin`, and a Kokoro venv in `~/Library/Application Support/batuta-tts/` (see `docs/workflow.md`).
