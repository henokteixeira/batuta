# Findings wait for round close

2026-09-08

An agent that notices something outside its slice writes one line in the findings note, and nothing else happens in that round: no ticket, no label, no plan change, no dispatch, however urgent. At round close the Orchestrator marks each line "⇒ candidate" or "⇒ recommend discard" and deletes nothing; only the Definer, with Henok, turns a line into a ticket or discards it. A production emergency is the single exception, and even then it is one line in "for you" and Henok decides.

Considered options: the Orchestrator ticketing findings the same day, rejected because that is how ENG-908 was dispatched undefined on 2026-09-08.

2026-09-11: the Definer opens every session by reading the findings note itself and putting the marked lines that still stand to Henok, so he does not have to remember to ask; this widens nothing under ADR 0005, since the findings came from rounds he opened and each line is his decision. A finding that falls on the code paths of a ticket already defined and waiting for a manifest is folded onto it; one that touches none becomes a ticket of its own.
