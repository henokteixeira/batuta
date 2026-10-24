# Orchestrator: rare branches — Batuta

Part of your role, `roles/orchestrator.md`. Follow a section whole when it happens.

## Production emergency

One of four measured facts: production down or returning errors to users; production data lost or corrupted; a secret or personal data exposed; money spent or charged wrongly. Anything else is a finding.

Write one line in `for you`: `Emergency: <the fact>. Open an emergency slice? Recommend <yes|no>.` Do nothing else. If Henok opens one, the Definer defines the ticket and appends `emergency: <ticket>` to the round note; on Henok's `emergency` you dispatch it next, inside the concurrency limit.

## A PR Henok closes without merging

His reason goes on the ticket, and the ticket goes back to the Definer. A slice held behind that PR goes back too, as `held behind PR #N: <ticket>` in the state note.

## `close the round` with a slice still working

A slice with a PR open finishes to waiting Henok. Any other slice stops: restart its executor, keep its worktree, write `not finished: <ticket>, worktree at <path>` in the state note. A held slice is written `held behind PR #N: <ticket>`. Both go back to the Definer.
