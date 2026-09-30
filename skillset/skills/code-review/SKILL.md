---
name: code-review
description: "Review the changes since a fixed point (commit, branch, tag, or merge-base) along three axes: Standards (does the code follow this repo's documented coding standards?), Spec (does the code match what the originating issue/spec asked for?) and Attack (what input or sequence makes this change produce a wrong result?). Runs the three reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to \"review since X\"."
---

Three-axis review of the diff between `HEAD` and a fixed point the user supplies:

- **Standards**: does the code conform to this repo's documented coding standards?
- **Spec**: does the code faithfully implement the originating issue / spec?
- **Attack**: what input, sequence or state makes this change produce a wrong result?

The three axes run as **parallel sub-agents** so they don't pollute each other's context, then this skill aggregates their findings.

Standards and Spec both ask whether the change matches something written down. Attack asks nothing of the kind: it assumes the change is wrong and goes looking for the case that proves it. Without that axis a review confirms the spec, and a case the spec never mentioned survives every gate.

The issue tracker is described in the `Issue tracker` section of the global CLAUDE.md (Linear, team Engineering).

## Process

### 1. Pin the fixed point

Whatever the user said is the fixed point (a commit SHA, branch name, tag, `main`, `HEAD~5`, etc.). If they didn't specify one, ask for it.

Capture the diff command once: `git diff <fixed-point>...HEAD` (three-dot, so the comparison is against the merge-base). Also note the list of commits via `git log <fixed-point>..HEAD --oneline`.

Before going further, confirm the fixed point resolves (`git rev-parse <fixed-point>`) and the diff is non-empty. A bad ref or empty diff should fail here, not inside two parallel sub-agents.

### 2. Identify the spec source

Look for the originating spec, in this order:

1. Issue references in the commit messages (`#123`, `Closes #45`, GitLab `!67`, etc.), fetched via the workflow in `docs/agents/issue-tracker.md`.
2. A path the user passed as an argument.
3. A spec file under `docs/`, `specs/`, or `.scratch/` matching the branch name or feature.
4. If nothing is found, ask the user where the spec is. If they say there isn't one, the **Spec** sub-agent will skip and report "no spec available".

### 3. Identify the standards sources

Anything in the repo that documents how code should be written, such as `CODING_STANDARDS.md` or `CONTRIBUTING.md`.

On top of whatever the repo documents, the Standards axis always carries the **smell baseline** below: a fixed set of Fowler code smells (_Refactoring_, ch.3) that applies even when a repo documents nothing. Two rules bind it:

- **The repo overrides.** A documented repo standard always wins; where it endorses something the baseline would flag, suppress the smell.
- **Always a judgement call.** Each smell is a labelled heuristic ("possible Feature Envy"), never a hard violation. Like any standard here, skip anything tooling already enforces.

Each smell reads *what it is* → *how to fix*; match it against the diff:

- **Mysterious Name**: a function, variable, or type whose name doesn't reveal what it does or holds. → rename it; if no honest name comes, the design's murky.
- **Duplicated Code**: the same logic shape appears in more than one hunk or file in the change. → extract the shared shape, call it from both.
- **Feature Envy**: a method that reaches into another object's data more than its own. → move the method onto the data it envies.
- **Data Clumps**: the same few fields or params keep travelling together (a type wanting to be born). → bundle them into one type, pass that.
- **Primitive Obsession**: a primitive or string standing in for a domain concept that deserves its own type. → give the concept its own small type.
- **Repeated Switches**: the same `switch`/`if`-cascade on the same type recurs across the change. → replace with polymorphism, or one map both sites share.
- **Shotgun Surgery**: one logical change forces scattered edits across many files in the diff. → gather what changes together into one module.
- **Divergent Change**: one file or module is edited for several unrelated reasons. → split so each module changes for one reason.
- **Speculative Generality**: abstraction, parameters, or hooks added for needs the spec doesn't have. → delete it; inline back until a real need shows.
- **Message Chains**: long `a.b().c().d()` navigation the caller shouldn't depend on. → hide the walk behind one method on the first object.
- **Middle Man**: a class or function that mostly just delegates onward. → cut it, call the real target direct.
- **Refused Bequest**: a subclass or implementer that ignores or overrides most of what it inherits. → drop the inheritance, use composition.

### 4. Spawn the three sub-agents in parallel

**Standards sub-agent prompt** should include:

- The full diff command and commit list.
- The list of standards-source files you found in step 3, **plus the smell baseline from step 3** pasted in full (the sub-agent has no other access to it).
- The brief: "Report, per file/hunk where relevant, (a) every place the diff violates a documented standard: cite the standard (file + the rule); and (b) any baseline smell you spot: name it and quote the hunk. Distinguish hard violations from judgement calls: documented-standard breaches can be hard, but baseline smells are always judgement calls, and a documented repo standard overrides the baseline. Skip anything tooling enforces. Under 400 words."

**Spec sub-agent prompt** should include:

- The diff command and commit list.
- The path or fetched contents of the spec.
- The brief: "Report: (a) requirements the spec asked for that are missing or partial; (b) behaviour in the diff that wasn't asked for (scope creep); (c) requirements that look implemented but where the implementation looks wrong. Quote the spec line for each finding. Under 400 words."

**Attack sub-agent prompt** should include:

- The diff command and commit list.
- The spec, when there is one, marked as the description of intent and not as the definition of correct.
- The **high-risk classes the diff touches** and their lenses, pasted in full from the list below. A diff touches a class when it changes a migration or a schema, transforms or deletes customer data, changes authentication or authorisation, changes money or billing, changes a public API contract, changes a third-party integration, or changes concurrency or a queue.
- The brief: "You are not reviewing this change. You are trying to make it produce a wrong result. Report only concrete failure scenarios: the input, state or sequence; the step that goes wrong; and what happens instead of what should happen. End each one with the single line of evidence that would confirm it. Do not report style, naming, missing tests, or anything you cannot state as a scenario. Look first at: a value at or past a boundary; a second call, a retry, or two callers at once; another route, job, command or migration that reaches the same rule or the same data without this change; an error path that is swallowed; a value that is absent, empty, zero, negative or very large; state and rows that already exist. If you find nothing, say so and name the three things you tried hardest to break. Under 400 words."

The lenses, by class:

- **Migration or schema**: what happens to the rows that already exist, and what the code still running does against the new schema during the deploy.
- **Customer data transformed or deleted**: what a half-finished run leaves behind, and what of it is not recoverable.
- **Authentication or authorisation**: every other route, job, command or export that reaches the same resource, and whether each one carries the check this change added.
- **Money or billing**: rounding, currency, a retry that charges twice, an amount that is zero, negative or absent.
- **Public API contract**: what an existing caller sends today that stops working, and what it now receives.
- **Third-party integration**: the call that times out, returns an error, or returns a shape nobody expected.
- **Concurrency or queue**: two callers at once, a message delivered twice, a job or an app killed half-way, a response lost after the server acted, an event that lands after the state moved on.

If the spec is missing, skip the Spec sub-agent and note this in the final report. Attack still runs: it needs the code, not the spec.

### 5. Aggregate

Present the three reports under `## Standards`, `## Spec` and `## Attack` headings, verbatim or lightly cleaned. Do **not** merge or rerank findings, because the axes are deliberately separate (see _Why three axes_).

End with a one-line summary: total findings per axis, and the worst issue _within each axis_ (if any). Don't pick a single winner across axes: that's the reranking the separation exists to prevent.

## Why three axes

A change can pass one axis and fail another:

- Code that follows every standard but implements the wrong thing → **Standards pass, Spec fail.**
- Code that does exactly what the issue asked but breaks the project's conventions → **Spec pass, Standards fail.**
- Code that follows every standard and does exactly what the issue asked, on a case the issue never mentioned → **Standards pass, Spec pass, Attack fail.**

Reporting them separately stops one axis from masking the others. The third is the one that does not ask permission from a document: Standards and Spec can only find a change guilty of disagreeing with something already written, and the expensive defects are the ones nothing was written about.
