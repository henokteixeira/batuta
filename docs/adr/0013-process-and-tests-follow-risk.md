# Process and tests follow risk

2026-10-24

The same heavy flow ran for a copy change and for a domain rule, and every acceptance case became a new test. In shema-api, the test cases went from 996 to 4,270 in ten weeks, to 121k lines of tests against 78k of production. Some of those tests asserted only that a value existed or that a mock was called.

Each ticket now has a track. A light ticket (estimate 1 or 2, low risk, no domain rule) gets no written plan and no Reviewer. A full ticket gets both. The Definer proposes the track and Henok confirms it. Every behaviour change is covered by a test, new or changed, and an existing test is extended before a new one is written. Critical code (a domain rule, money, data, auth, state and lifecycle) gets a test per invariant, and its tests are falsified by hand, once. A trivial change gets no test. This narrows ADR 0009 (invariants only for critical code) and ADR 0011 (falsification by the Reviewer, only for critical code).
