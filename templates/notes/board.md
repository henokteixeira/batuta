# board

One line per slice of the open round, in manifest order: `<codename> · <ticket> · <state> · <model>`. States: recon, grilling, implementing, reviewing, PR open, CI, verified, waiting Henok, merged. The concurrency limit: at most two slices in flight, a third only when it belongs to a ticket already in flight. The Orchestrator edits by substring and empties the board at round close; history goes to the `state ·` note, the manifest is in the `round` note.

(no slice in flight)
