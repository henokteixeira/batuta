# how it works

In one sentence: you define with the Definer, the Orchestrator executes, and you only answer what is in "for you".

## Before each round

1. Open the Definer and bring the list: undefined tickets, defects seen in a test, ideas, and the "Define:" lines the Orchestrator left in "for you". It works for what is already in Linear and for what is not a ticket yet.
2. It grills item by item, one frontier at a time, each question with the recommended answer. Answer by voice. Facts it finds; only decisions come to you.
3. It updates the glossary, writes an ADR when a decision is hard to reverse, publishes spec and tickets to Linear with blockers, and labels `ready-for-agent` only what has a one-sentence rule, a testable acceptance criterion and zero open decisions.

## During the round

4. Tell the Orchestrator to start. It pulls `ready-for-agent` tickets with no blocker, writes the slice plan, creates the worktree, recruits an executor with the ticket's model and dispatches. Three tasks at most, one grilling you at a time.
5. You only look at "for you". Each line is a closed question or a high-risk approval. Answer there and the line goes away. The board shows progress.
6. The Orchestrator verifies each PR against the tests and against the spec, waits for CI, records decisions on the ticket and restarts the executor. Visible changes you check in the portal or simulator.

## At the end

7. It writes the state note in the logs stack and ends with TASK_COMPLETE or BLOCKED. Findings become tickets or are discarded.
8. Clear the context yourself: once the Orchestrator ends with TASK_COMPLETE or BLOCKED, type `/clear` in its terminal; same for the Definer at the end of a definition session, after its `definition · <date>` note. Executors are restarted by the Orchestrator. Never leave it to auto-compact. The next round starts from the state note; the notes are the memory, the session is not.

## High parallelism

Ask the Definer for a high-autonomy round. It closes the whole queue first and writes `mode: high autonomy` on the board. The Orchestrator fires the whole frontier at once and deletes the line when it closes. Never the default.

## Voice

The Definer writes its spoken frontier to ~/.cache/grill/Definidor.txt and tells you to run `grill-voice Definidor` in the voice terminal. Hold Space to talk, Enter to accept, `e` to edit, `r` to re-record.

Full text: ~/Documents/programming/batuta/docs/workflow.md
