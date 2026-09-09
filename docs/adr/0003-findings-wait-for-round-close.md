# Findings wait for round close

2026-09-08

An agent that notices something outside its slice writes one line in the findings note, and nothing else happens in that round: no ticket, no label, no plan change, no dispatch, however urgent. At round close the Orchestrator marks each line "⇒ candidate" or "⇒ recommend discard" and deletes nothing; only the Definer, with Henok, turns a line into a ticket or discards it. A production emergency is the single exception, and even then it is one line in "for you" and Henok decides.

Considered options: the Orchestrator ticketing findings the same day, rejected because that is how ENG-908 was dispatched undefined on 2026-09-08.
