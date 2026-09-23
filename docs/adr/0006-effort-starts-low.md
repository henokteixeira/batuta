# Effort starts low

2026-09-23

The Definer and the Orchestrator ran on Fable with effort `max`, and executors got more effort the less context they would see. Anthropic's documentation says effort governs every output token, tool calls included, and Claude Code's documentation says `max` is prone to overthinking and recommends `high`. Matt Pocock argued on X on 2026-07-15 for starting low and raising effort only when a run shows it is needed. In the Shema workspace, from 2026-09-08 to 2026-09-23, the Orchestrator never actually ran at `max`. Effort now starts low: Definer and Orchestrator at `high`, executors at `low` or `medium` by estimate and risk. `max` comes only after a round shows a reasoning failure, recorded in the state note; an executor goes up one level only when it fails or stalls, re-dispatched from its plan on disk, with the reason in its log note.

This reverses commit 62bb412, which put the Definer and the Orchestrator always on Fable with effort `max`.

Considered options: keeping `max` on top, rejected because it spends tokens on overthinking that no round showed was needed.
