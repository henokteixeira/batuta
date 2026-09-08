---
name: cleaning-mac-disk-space
description: Use when the Mac is running out of disk space, or when asked to free space, clean caches, remove build artifacts, prune git worktrees, or find leftovers from uninstalled apps - diagnoses first, classifies by risk, never deletes without confirmation
---

# Cleaning Mac Disk Space

Reconstructed on 2026-09-08 after the original was removed by a skillset switch. Same contract: diagnose first, classify by risk, delete nothing without explicit confirmation.

## Process

1. **Measure before touching anything.** `df -h /` for the headline, then `du -sh` over the usual suspects, largest first: `~/Library/Caches/*`, `~/Library/Developer/Xcode/DerivedData`, `~/Library/Developer/CoreSimulator/Devices`, `~/.npm/_cacache`, `~/.npm/_npx`, `~/.pnpm-store`, `~/Library/pnpm`, `~/.cache`, `~/.pub-cache`, `~/.gradle/caches`, `~/.cocoapods`, `~/Library/Application Support/*`, `~/Library/Logs`, `~/.Trash`, Docker (`docker system df`), Homebrew (`brew cleanup -n`), and every `node_modules`, `.dart_tool`, `build`, `.venv` or `.worktrees` under the user's project directories (`find ~/Documents/programming -maxdepth 4 -type d \( -name node_modules -o -name .dart_tool -o -name build -o -name .venv \) -prune -exec du -sh {} +`). Git worktrees: `git worktree list` per repo, flag the ones whose branch is merged or deleted.
2. **Classify every candidate by risk** and present a table: size, path, what regenerates it, risk.
   - **Safe**: caches that regenerate on demand (package manager caches, DerivedData, simulator logs, Homebrew downloads, `.Trash`).
   - **Check first**: build outputs and `node_modules` of projects still in use (regenerate with an install, but cost time); simulators with no recent boot; worktrees whose branch is merged.
   - **Never on your own**: anything under `~/Documents`, `~/Desktop`, app data in `Application Support`, databases, `.env` files, keychains, anything the user did not name.
3. **Ask, then act.** Show the table with the total reclaimable by tier and ask which tiers to delete. Delete only what the user confirmed, one tier at a time, with the exact command printed before running it. Prefer the tool's own cleanup (`brew cleanup`, `docker system prune`, `xcrun simctl delete unavailable`, `git worktree prune`, `npm cache clean --force`) over `rm -rf`.
4. **Measure again** and report freed space per tier.

## Rules

- Never delete without confirmation, even for the safe tier.
- Never touch a git worktree that has uncommitted changes; report it instead.
- Leftovers from uninstalled apps: look in `~/Library/Application Support`, `~/Library/Preferences`, `~/Library/Caches`, `~/Library/Containers` for bundles whose app no longer exists in `/Applications`; list them, do not remove them unprompted.
- Report in the user's language, sizes in human units, paths relative to `~`.
