# Henok merges every PR

2026-09-08

No agent merges. A verified, green PR becomes a "Review and merge PR #N" line in "for you" and its item is waiting Henok; the Orchestrator learns of the merge from GitHub, never by asking Henok. The merge is the last point where a human sees the change, so it stays with him.

Considered options: an agent merging once it has verified the PR, rejected because a green PR is verified, not reviewed.
