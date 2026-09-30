# Everything for Henok is short

2026-09-30

Everything written for Henok is short and written for a human: chat, notes, PRs, tickets, reviews and commits. A PR body has four sections (why, what changes, Test by hand, size) and about 200 words; a ticket has a fixed shape that opens with its context; the Orchestrator's review opens with a one-line verdict and folds its evidence under `<details>`. PRs stay under 300 changed lines, tests excluded, up to 500 when they cannot split, and say why when larger. The last fifteen PRs of the room app ran from 197 to 1,734 words, full of commit hashes and internal names written for the Orchestrator, and up to +892 lines; Henok could explain little of what shipped. The old rule exempted tickets, PRs and commits from concision, which is how they grew.

Considered options: a hard cap on PR size, rejected by Henok in favour of a practice with a stated reason for exceptions; evidence only in the slice log, rejected because reviewers would lose the proof.
