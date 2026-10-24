# Batuta

Batuta is Henok's workflow for agents on a Maestri canvas: how work is defined, batched into a round, dispatched, and merged. These are its words; the roles, the templates, the plans, the tickets and the commits use no others. Linear's own state names (Todo, In Progress, In Review, Done) stay as Linear writes them.

## Language

### The round

**Round**:
One batch of work. It opens when Henok says "go" over a written manifest and closes when every item on that manifest is merged or waiting Henok and no slice is held, or when Henok says "close the round".
_Avoid_: sprint, cycle, iteration, milestone

**Manifest**:
The ordered list of tickets a round runs: one cluster, in the order Henok gives. The Definer writes it with Henok before "go".
_Avoid_: queue, plan, to-do list

**Cluster**:
Tickets connected by `blockedBy` edges or touching the same area or app, run as one manifest. Its size follows the connections, never a fixed number.
_Avoid_: bundle, epic, the three tickets

**Manifest item**:
One line of the manifest: a leaf ticket, or a parent whose unblocked children are its slices. A parent counts as one item.
_Avoid_: entry, task, story

**Slice**:
What one executor runs: one ticket, one worktree, one PR.
_Avoid_: task, job, unit of work

**In flight**:
The state of a slice from dispatch until its PR is reviewed and green, or it is waiting Henok.
_Avoid_: running, active, in progress, WIP

**Waiting Henok**:
The state of an item whose next step is Henok's. A line for it exists in "for you", and its slot is free.
_Avoid_: blocked, blocked on Henok, stuck

**Held slice**:
A slice that touches a source file an earlier slice of the round touches. It is dispatched only after the earlier PR is merged, and it keeps the round open.
_Avoid_: blocked slice, queued slice, stacked slice

**Follow-up slice**:
A new slice on a ticket whose PR is already merged, dispatched in the same round to fix a defect in that PR's code. It is the same manifest item, not new work.
_Avoid_: hotfix, fix ticket, patch PR

**Concurrency limit**:
At most three slices in flight at once.
_Avoid_: WIP limit, parallelism cap

**Emergency slice**:
A production emergency Henok decides to act on: its ticket is appended to the round note as `emergency: <ticket>` and dispatched next, inside the concurrency limit; with no round open it is a one-item manifest.
_Avoid_: hotfix round, incident, firefight

### The notes

**Round note**:
The standing note named "round" that holds the manifest of the open round. Outside a round its body reads "(no round open)".
_Avoid_: manifest note, dated round note, the round file

**State note**:
The "state · <date>" note written in the logs stack when a round closes: what merged, what waits Henok, what is blocked and why, what did not finish, defects by origin, hot files, and a short retro.
_Avoid_: handoff, report, summary

**Logs stack**:
The stack of notes that holds "log · <codename>", "state · <date>" and "definition · <date>". Measurements, history and status live there and nowhere else.
_Avoid_: archive, journal, history note

**For you**:
The standing note holding only what is still pending on Henok, one `- [ ]` checkbox per item. Henok ticks a line he did or answers it with `R: …`; the agent that wrote it records that on the ticket and deletes the line. No agent ever ticks a line for him.
_Avoid_: inbox, to-do, blockers, action items

**Findings**:
The standing note of defects that existed before the round, one line each with its origin. Lines the round fixed are deleted at once; the rest are marked at round close and the Definer empties the note with Henok after.
_Avoid_: issues note, bug list, parking lot

**Review and merge line**:
The line in "for you" that hands Henok a reviewed, green PR: "Review and merge <PR URL> — <ticket> (unblocks: …)". Henok answers it by merging, or with "R: changes: <what>", which re-dispatches the ticket.
_Avoid_: approval, review request, merge task

**Define: line**:
The line in "for you" that sends a manifest ticket back to the Definer, naming what is missing. The ticket is skipped and resumes in the same round once the Definer has labelled it, or goes to the next manifest if the round closed first.
_Avoid_: blocker note, clarification, question

**Test by hand**:
The block of the PR body that says what Henok does to see the change working and what he must see, or why there is nothing to test by hand.
_Avoid_: manual test, QA, smoke test, Look line

### People and terminals

**Definer**:
The terminal Henok talks to. It defines, publishes tickets, applies the ready-for-agent label, and writes the manifest with him. Definidor on the canvas.
_Avoid_: planner, product manager, spec writer

**Front door**:
The Definer's standing as the single entry for everything Henok brings. Nothing enters the flow any other way.
_Avoid_: intake, triage, entry point

**Orchestrator**:
The terminal that dispatches the round: it routes each manifest ticket to an executor, sends full-track PRs to a reviewer, and keeps "for you" and the round note. It never plans, edits or reviews. Orquestrador on the canvas.
_Avoid_: manager, lead, queue runner

**Executor**:
The agent that runs one ticket, from its own plan to the PR, and dies with the PR.
_Avoid_: worker, implementer, dev agent

**Reviewer**:
The agent that reviews one full-track PR knowing only the ticket and the diff: three axes, falsification of the critical tests, one review on the PR. It never edits and dies with the PR. Revisor on the canvas.
_Avoid_: checker, verifier, QA

**Question round**:
One frontier of grilling questions, each with its recommended answer first: at most four to a call, the rest in the calls that follow.
_Avoid_: round (that is the batch of work), interview, Q&A session

### Work items

**Track**:
How much process a ticket gets. Light: estimate 1 or 2, low risk, no domain rule; no written plan, the automated GitHub review. Full: everything else; a written plan and the Reviewer. The Definer proposes it, Henok confirms.
_Avoid_: lane, tier, mode

**Critical code**:
A domain rule, money, data, auth, or state and lifecycle. It gets a test per invariant, and its tests are falsified by hand.
_Avoid_: core, important code, hot path

**Small ask**:
Something Henok wants that carries no open decision. The Definer defines it in one exchange, with Henok confirming its rule, and it waits for the next manifest.
_Avoid_: quick fix, tiny task, drive-by

**Finding**:
A defect an agent noticed that existed before the round: one line in the findings note until the round closes. A defect in code the round changed is fixed in the round, and is never a finding.
_Avoid_: issue, bug report, side quest, TODO

**Invariant**:
A rule about an interface of critical code that must hold after every event, including a kill, a lost response and a retry. Henok decides it, and each one is a test in the acceptance criterion.
_Avoid_: constraint, assumption, edge case

**Origin**:
The PR that introduced a defect, traced in git, or "gap" when the behaviour was never handled. Never taken from what a ticket or a report says.
_Avoid_: root cause, culprit, pre-existing

**Hot file**:
A source file two or more of a round's defects trace to. The state note names it, and the Definer recommends a refactor of the hottest.
_Avoid_: hotspot, problem file, god file

**Backlog**:
Every ticket in Linear that nobody brought to the Definer. It is never listed, audited or dispatched.
_Avoid_: queue, pool, the rest of the tickets

**Production emergency**:
One of four measured facts, never a judgement: production is down or returning errors to users; production data is being lost or corrupted; a secret or personal data is exposed; money is being spent or charged wrongly.
_Avoid_: urgent, critical, incident, P0
