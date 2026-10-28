# The executor plans, and a stranger reviews

2026-10-24

Every hop between agents lost information: the Orchestrator rewrote each ticket as a plan, the executor implemented it, and the Orchestrator verified it again with the author's context in mind. The Orchestrator now only dispatches. It routes each manifest ticket to an executor, which plans from the ticket itself. No agent reviews its own work: a full-track PR goes to a Reviewer that knows only the ticket and the diff, and a light-track PR gets the automated GitHub review. The Orchestrator runs on sonnet at effort medium, since dispatch needs no deep reasoning; this replaces ADR 0007.

The round machinery shrank with it: the board and "how it works" notes, the three routines, the high-autonomy round and the Orchestrator's own falsification are gone. The manifest, "for you", findings, held slices (ADR 0008) and in-round fixes stay.

Considered options: two roles, with the Definer dispatching, rejected because the Definer would carry execution context again; Henok dispatching by hand, rejected as manual work with no gain.

Amended 2026-10-28: the high-autonomy round is back, at Henok's request. When the round note says so, the concurrency limit gives way to the machine's free memory; held slices and the one-grilling limit stay.
