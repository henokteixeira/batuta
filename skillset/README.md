# High Autonomy Nori Skillset

## Overview

A high-parallelization, high-autonomy skillset designed for building software at scale with AI agents. Agents operate with full autonomy to accomplish stated goals — the only guardrails are no changes to production data, main, or third-party APIs. If you're new to agentic programming, this is a good starting configuration.

## Key Tenets

**1. Aggressive Parallelization**

Rather than sequentially watching a single agent work, this skillset is designed for spawning multiple concurrent Claude Code sessions using tmux, terminal tabs, or multiple windows. Git worktrees provide isolated workspaces so agents don't conflict with each other. The human engineer rotates between sessions, reviewing completed work and feeding new tasks to idle agents.

**2. Test-Driven Development**

Agents must write tests before implementation. This provides a formalized specification that prevents context degradation over long conversations and creates safety rails for future modifications. Tests function as executable documentation of requirements.

**3. Strong Documentation**

Since agents don't retain learning across sessions, institutional memory is maintained through:
- Colocated `docs.md` files updated whenever code changes
- A knowledge base that agents can query for context

## How to Use This Skillset

The standard workflow:

1. **Run many agents in parallel.** Open several terminal tabs or tmux panes, each running Claude Code with this skillset. Most should run in "yolo mode" for maximum autonomy.

2. **Review plans carefully.** Each agent will research and present a plan before implementation. This plan should be reviewed in depth—it's your primary checkpoint before code is written.

3. **Let agents work autonomously.** Once a plan is approved, agents will use TDD to implement features, update documentation, and create a PR.

4. **Review code at PR time.** All code should be reviewed during code review, once the agent has given you a PR. This is where you catch issues, not during implementation. You must be ok with closing PRs.

Agents are designed to follow a full workflow: worktree creation → research → planning → test-first development → documentation updates → PR creation. The aim is to have the agent one-shot as many problems as possible. You can also use this skillset to do implementation exploration by running many agents on the same problem with slightly different implementation suggestions to see which you prefer.
