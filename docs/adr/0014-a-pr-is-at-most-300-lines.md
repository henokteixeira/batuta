# A PR is at most 300 lines

2026-10-24

Henok reviews every PR himself (ADR 0004), and he can only do that for a small one. A PR holds at most 300 hand-written lines changed, code and tests together. Generated files, such as migrations, lockfiles, snapshots and generated code, do not count, and the PR lists them. The Definer splits any work that will not fit before it is labelled. This replaces the softer practice of under 300 lines with tests excluded and up to 500 allowed.
