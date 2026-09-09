---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **question rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one question round: number each question and give your recommended answer. Then wait for the user's answers before the next question round.

Format a question round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

## How to ask

When the user is at the keyboard in Claude Code and you are the terminal he talks to, ask the frontier through the AskUserQuestion tool: at most four questions per call, each with two to four options, the recommended option first and marked "(Recommended)". A frontier of more than four questions goes in consecutive calls of the same question round.

The text format above is the fallback: use it by voice, when writing `~/.cache/grill/<agent>.txt`, and when the asker is an agent talking to another agent. An Orchestrator relaying an executor's frontier writes it in the "for you" note and never uses the tool.

Each question round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next question round. A question whose answer depends on another question still open in this question round belongs to a _later_ one, not this one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent to find it; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.
