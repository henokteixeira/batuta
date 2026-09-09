# Batuta

Batuta is Henok's workflow for agents on a Maestri canvas: how work is defined, batched into a round, dispatched, and merged. These are its words; the roles, the templates, the plans, the tickets and the commits use no others.

## Language

### The round

**Round**:
One batch of work. It opens when Henok says "go" over a written manifest and closes when every item on that manifest is merged or waiting Henok, or when Henok says "close the round".
_Avoid_: sprint, cycle, iteration, milestone

**Manifest**:
The ordered list of tickets a round runs, at most three except in a high-autonomy round, written by the Definer with Henok before "go".
_Avoid_: queue, plan, to-do list

**Manifest item**:
One line of the manifest: a leaf ticket, or a parent whose unblocked children are its slices. A parent counts as one item.
_Avoid_: entry, task, story

**Slice**:
What one executor runs: one plan, one worktree, one PR.
_Avoid_: task, job, unit of work

**In flight**:
The state of a slice from dispatch until it is verified green or waiting Henok.
_Avoid_: running, active, in progress, WIP

**Waiting Henok**:
The state of an item whose next step is Henok's. A line for it exists in "for you", and its slot is free.
_Avoid_: blocked, blocked on Henok, stuck

**Concurrency limit**:
At most two slices in flight at once; three only when the third belongs to a ticket that already has a slice in flight.
_Avoid_: WIP limit, the limit of three, parallelism cap

**High-autonomy round**:
A round Henok asks for, whose manifest is the whole frontier the Definer closed with him, dispatched at once. The three-ticket cap and the concurrency limit are suspended for that round alone.
_Avoid_: autonomous mode, yolo mode, full autonomy

**Emergency round**:
The emergency slice Henok opens for one production emergency: its ticket is appended to the round note, dispatched ahead of the manifest order inside the concurrency limit, and closes with the round it joined; with no round open it is a one-item manifest.
_Avoid_: hotfix round, incident, firefight

### The notes

**Round note**:
The standing note named "round" that holds the manifest of the open round. Outside a round its body reads "(no round open)".
_Avoid_: manifest note, dated round note, the round file

**State note**:
The "state · <date>" note written in the logs stack when a round closes: what merged, what waits Henok, what is blocked and why, what was measured, what did not finish, and the manifest itself.
_Avoid_: handoff, report, summary, retro

**Logs stack**:
The stack of notes that holds "log · <codename>", "state · <date>" and "definition · <date>". Measurements, history and status live there and nowhere else.
_Avoid_: archive, journal, history note

**Board**:
The standing note with one line per slice of the open round, in manifest order. It is emptied at round close.
_Avoid_: kanban, dashboard, status board

**For you**:
The standing note holding only what is still pending on Henok, one plain bullet per item, never a checkbox.
_Avoid_: inbox, to-do, blockers, action items

**Findings**:
The standing note where each finding is one line. It only grows during a round; every line is marked at round close.
_Avoid_: issues note, bug list, parking lot

**How it works**:
The standing note that carries the rules of the workflow on the canvas, so the canvas explains itself.
_Avoid_: readme note, instructions, cheatsheet

**Review and merge line**:
The line in "for you" that hands Henok a verified, green PR: "Review and merge PR #N — <ticket> (unblocks: …)"; the Definer's glossary PR writes "glossary" in place of the ticket.
_Avoid_: approval, review request, merge task

**Define: line**:
The line in "for you" that sends a manifest ticket back to the Definer, naming what is missing. The ticket is skipped and resumes in the same round once the Definer has labelled it, or goes to the next manifest if the round closed first.
_Avoid_: blocker note, clarification, question

### People and terminals

**Definer**:
The terminal Henok talks to. It defines, publishes tickets, applies the ready-for-agent label, and writes the manifest with him. Definidor on the canvas.
_Avoid_: planner, product manager, spec writer

**Front door**:
The Definer's standing as the single entry for everything Henok brings. Nothing enters the flow any other way.
_Avoid_: intake, triage, entry point

**Orchestrator**:
The terminal that runs the round: it dispatches the manifest in order, verifies what comes back, and never edits a repository. Orquestrador on the canvas.
_Avoid_: manager, dispatcher, lead, queue runner

**Executor**:
The agent that runs one slice, from plan to PR, and dies with the PR.
_Avoid_: worker, implementer, dev agent

**Question round**:
One frontier of grilling questions, each with its recommended answer first: at most four to a call, the rest in the calls that follow.
_Avoid_: round (that is the batch of work), interview, Q&A session

**Voice session**:
One grill-voice run: the frontier spoken, each answer recorded and transcribed.
_Avoid_: voice round, voice call

### Work items

**Small ask**:
Something Henok wants that carries no open decision. The Definer closes it in one exchange, without a grilling session, and it waits for the next manifest.
_Avoid_: quick fix, tiny task, drive-by

**Finding**:
Something an agent noticed that does not belong to the slice it is on. It is one line in the findings note, never a ticket, a label, a plan change or a dispatch in the round it appeared.
_Avoid_: issue, bug report, side quest, TODO

**Backlog**:
Every ticket in Linear that nobody brought to the Definer. It is never listed, audited or dispatched.
_Avoid_: queue, pool, the rest of the tickets

**Production emergency**:
One of four measured facts, never a judgement: production is down or returning errors to users; production data is being lost or corrupted; a secret or personal data is exposed; money is being spent or charged wrongly.
_Avoid_: urgent, critical, incident, P0
