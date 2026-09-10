# how it works

In one sentence: you bring everything to the Definer, agree with it a round of at most three tickets, the Orchestrator runs that round and nothing else, and you answer what is in "for you" and merge every PR.

## Before each round

1. Open the Definer and bring everything: undefined tickets, defects seen in a test, ideas, small asks with no open decision, findings from the round that just closed, and the order you want them run. Only what you bring enters the flow; nobody audits the backlog or other people's tickets.
2. It grills item by item, one frontier per question round, each question with the recommended answer. Answer by voice. Facts it finds; only decisions come to you.
3. It updates the glossary, writes an ADR when a decision is hard to reverse, publishes spec and tickets to Linear with blockers, and labels `ready-for-agent` only what has a one-sentence rule, a testable acceptance criterion and zero open decisions. Only the Definer ever applies that label, and every ticket it labels, with either label, is assigned to you.
4. It writes the manifest with you in the `round` note: at most three tickets, in the order they run. That note is the whole of the next round.

## During the round

5. Say "go" to the Orchestrator. It dispatches only the manifest, in that order: writes the slice plan, creates the worktree, recruits an executor with the ticket's model and dispatches. The concurrency limit: at most two slices in flight, a third only when it belongs to a ticket already in flight; one grilling you at a time. It never pulls other `ready-for-agent` tickets, findings, urgent items or anything you mention in passing. A manifest ticket it cannot dispatch gets a `Define:` line in "for you" and is skipped; once the Definer has defined it, it resumes in the same round. The only things you say to the Orchestrator are "go", "close the round", "emergency" and your answers to the lines it wrote in "for you"; anything else gets one line back: take it to the Definer.
6. You only look at "for you". Each line is a closed question, an approval, a `Define:` to carry to the Definer, something to look at, a script to run, a PR to review and merge, or an emergency to decide. Answer by appending `R: …` to the line, or by voice. Answer it or do it and the line is deleted, never ticked. Measurements and history live in the logs stack; the board shows the round's slices.
7. The Orchestrator verifies each PR against the tests and against the spec, waits for CI, records decisions on the ticket, writes `Review and merge PR #N` in "for you" and restarts the executor. Every PR an agent opens is assigned to you, and you merge every one yourself; no agent merges. Findings wait in "findings" until the round closes. Visible changes you check in the portal or simulator.

## At the end

8. The round closes when every manifest item is merged or waiting Henok — an open `Review and merge PR #N` line counts — or when you say "close the round". The Orchestrator records the decisions, marks each finding `⇒ candidate` or `⇒ recommend discard`, writes the `state · <date>` note in the logs stack, empties the board, sets the `round` note back to `(no round open)` and ends with TASK_COMPLETE or BLOCKED: waiting on Henok. After that note it answers questions and does post-merge bookkeeping; it dispatches nothing, however small and whoever asks.
9. Clear the context yourself: type `/clear` in the Orchestrator after the state note and not before; same for the Definer after its `definition · <date>` note and the next manifest. Executors are restarted by the Orchestrator. Never leave it to auto-compact. The next round starts from a new manifest, then `/clear` and "go"; the notes are the memory, the session is not.

## Mid-round asks and emergencies

Anything new mid-round goes to the Definer and waits for the next manifest; it never joins the round already running. A production emergency is one of four measured facts — production down or returning errors, data lost or corrupted, a secret or personal data exposed, money spent or charged wrongly — and reaches you as one line in "for you" with a recommendation. You decide. If you open it, the Definer defines the ticket in one exchange and appends it to the manifest, you say "emergency" to the Orchestrator, and that slice runs next. Anything else that looks urgent is a finding.

## High autonomy

Ask the Definer for a high-autonomy round. It closes everything you brought and writes the whole frontier into the `round` note, with `mode: high autonomy` under the date. For that round only, the three-ticket cap and the concurrency limit are suspended: the Orchestrator fires the manifest at once. The note goes back to `(no round open)` at close. Never the default.

## Voice

The Definer writes its spoken frontier to ~/.cache/grill/Definidor.txt and tells you to run `grill-voice Definidor` in the voice terminal. Hold Space to talk, Enter to accept, `e` to edit, `r` to re-record.

Full text: ~/Documents/programming/batuta/docs/workflow.md
