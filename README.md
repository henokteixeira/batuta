# batuta

The conductor's baton. This repository holds Henok's workflow for agents inside Maestri: the skillset, the terminal roles, the scripts and the templates. It is project-agnostic.

## Layout

- `skillset/` — the Nori skillset `personal/batuta`: the global CLAUDE.md (`AGENTS.md`), the skills (Nori's execution core plus Matt Pocock's definition skills) and the subagents. Linked into Nori with `nori-skillsets link`.
- `roles/` — the four Maestri roles. The preset in the app is only a pointer; the truth lives here.
  - `definer.md` — the front door: grills, defines tickets with the rule Henok confirmed, writes the manifest with him.
  - `orchestrator.md` — dispatches the manifest to executors and reviewers. Never plans, edits or reviews.
  - `executor.md` — one ticket: its own plan, TDD, a PR. Restarted after the PR.
  - `reviewer.md` — reviews a full-track PR knowing only the ticket and the diff.
- `bin/` — scripts:
  - `setup-canvas` — creates and wires the three standing notes and removes what older versions left.
  - `notify-maestri.sh` — Claude Code Notification hook that opens Maestri on click instead of Terminal.
- `templates/` — initial content of the canvas notes and the preset text.
- `docs/workflow.md` — how a round runs, from the manifest to Henok's merge and the state note.
- `docs/adr/` — the decisions that shaped the workflow. Read them before changing a role.
- `CONTEXT.md` — the glossary of the workflow itself: round, manifest, track, slice, finding.
- `test/` — `bash test/setup-canvas-test.sh`.
- `archive/notes/` — the notes from the old workspaces, exported on 2026-09-08, to be mined for ADRs and glossary entries.

## How the work splits

Henok brings everything to the Definer, confirms each ticket's rule and track, and orders the manifest. The Orchestrator dispatches it: each ticket to an executor that plans and opens a PR of at most 300 lines. A light ticket gets the GitHub review; a full one gets a Reviewer with no context. Henok merges every PR. Details in `docs/workflow.md`.

## Installing on a new machine

```
git clone git@github.com:henokteixeira/batuta.git ~/Documents/programming/batuta
nori-skillsets link ~/Documents/programming/batuta/skillset --name batuta
nori-skillsets switch personal/batuta
```

Then, in Maestri, create the four roles with the text in `templates/presets.md`. With the roles in place, run `bin/setup-canvas` in the Orchestrator terminal, with Maestro Mode on: it creates and wires the three standing notes. Point the Notification hook in `~/.claude/settings.json` to `bin/notify-maestri.sh`.
