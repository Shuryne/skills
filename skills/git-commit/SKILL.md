---
name: git-commit
description: Splits pending work into atomic commits and writes Conventional-Commits messages with Chinese subjects and why-focused bodies. Use whenever changes are about to be committed, when a working tree holds several unrelated changes, or when a commit message or commit history needs to be written, reworded or reorganized.
---

# Git Commit Conventions

## Output language

This document is English so it reads as a standalone reference. The commit messages it produces are
Chinese — subject and body only; type, scope and footer keywords stay English.

## Flow

When asked to commit:

1. Read the full picture first: `git status`, `git diff`, `git diff --staged`, and `git log --oneline -10`
   to match the repository's existing style.
2. Group the changes into atomic commits (rules below). Decide this independently — do not ask for
   confirmation of the split unless the changes are genuinely ambiguous or touch something risky.
3. Commit them one by one, in dependency order, staging explicit paths per commit.
4. Report the resulting commits.

Never push unless explicitly asked. Never rewrite history that has already been pushed.

## Splitting rules

**One commit = one complete logical change**, self-contained enough to be reverted on its own without
dragging unrelated work with it.

- **Structural and behavioral changes never share a commit.** Renames, extractions, file moves and
  formatting go in their own commit; the behavior change goes in another. This is the single most
  important rule when a large diff is on the table.
- **Cohesion decides, not file count.** A feature's endpoint, schema, service and tests belong in one
  commit — splitting them yields commits that don't stand alone. Two unrelated bug fixes in the same
  file are two commits.
- **Dependency order.** Foundations first (config, shared types, utilities), then the code that uses
  them, so every commit in the sequence is coherent on its own.
- **Split out incidental work**: drive-by fixes, dependency bumps, formatting, generated files.
  These are the commits that make a feature diff unreadable when left mixed in.
- **Do not split** what cannot stand alone. A commit that leaves the codebase broken is worse than a
  slightly larger commit — prefer correctness over granularity.

Staging:

- Stage explicit paths: `git add <path>...`. Never `git add -A` or `git add .` for a multi-commit split.
- When one file contains changes belonging to different commits, stage by hunk with `git add -p`.
- Verify with `git diff --staged` before each commit that only the intended change is staged.
- Never commit `.env`, secrets, logs, build output, or unrelated files that happen to be dirty.
- Never use `--no-verify`. If a hook fails, fix the cause.

## Message format

```
<type>(<scope>): <imperative subject, ≤50 characters, no trailing period>

<body: why the change was made, not what changed. Wrapped at 72 characters.>

<footer: BREAKING CHANGE / issue reference / tool trailer>
```

The 50-character subject limit is counted in characters, not words — a Chinese subject fits
considerably more than the English gloss of it suggests.

- Type and scope are English and lowercase; the subject and body are **Chinese by default**. Use
  another language only when explicitly asked, or when the repository's existing history is clearly
  in that language — consistency with the repo wins.
- Scope is optional; use the module or resource name (`auth`, `user`, `deps`), not a file path.
- The subject says what the commit does, imperatively — "fix the token not refreshing after login",
  never the past tense "fixed ...".
- The body explains **why**: the problem, the constraint, the reason this approach was chosen. Skip
  the body only when the subject is genuinely self-explanatory (typo fix, dependency bump).
- When a commit deliberately leaves related work undone, the body says so. It marks where the next
  commit starts, and stops a reviewer reading the omission as an oversight.
- Never restate the diff line by line in the body — the diff is already there.
- Breaking changes get a `BREAKING CHANGE:` footer describing the migration.

| Type       | Use for                                                          |
| ---------- | ---------------------------------------------------------------- |
| `feat`     | New user-visible capability                                       |
| `fix`      | Bug fix                                                           |
| `refactor` | Behavior-preserving restructuring                                 |
| `perf`     | Performance improvement                                           |
| `docs`     | Documentation only                                                |
| `test`     | Tests only                                                        |
| `build`    | Build system, dependencies, packaging                             |
| `ci`       | CI configuration                                                  |
| `chore`    | Housekeeping that fits nothing above                              |

## Reorganizing existing commits

Only on unpushed history:

- Fixing the latest message: `git commit --amend`.
- A change belonging to an earlier commit: `git commit --fixup=<sha>` then
  `git rebase -i --autosquash <base>`.
- Splitting a commit that is already made: `git reset --soft HEAD~1`, then stage and commit in
  logical units with `git add -p` until the working tree is clean.

## Before each commit

1. Does this commit do exactly one thing?
2. Does it mix structural and behavioral changes?
3. Would it leave the codebase in a working state on its own?
4. Is anything staged that belongs to a different commit, or should not be committed at all?
5. Does the subject read as an imperative Chinese sentence under 50 characters, with the right type?
6. Does the body explain why, and would it still make sense to someone reading it six months later?
