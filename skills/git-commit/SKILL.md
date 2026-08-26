---
name: git-commit
description: Plan and create reviewable atomic Git commits from authorized local changes while following repository conventions. Use only when the user explicitly asks to commit changes; do not use merely because a task has finished.
---

# Git Commit

Inspect all authorized staged, unstaged, and untracked changes before staging. Read repository guidance and recent commits for the established message format and language. Preserve unrelated work and treat the existing index as user state.

Before mutating the index, present an ordered commit plan with each group's intent, paths or hunks, and dependencies. Proceed without waiting unless the grouping is genuinely ambiguous, risky, or would alter already-staged user state.

Use the review and revert boundary, not the feature label or file count, to choose groups:

- Changes with different reviewer concerns or different reasons to revert must be separate, even when they support the same end-to-end feature.
- Keep structural changes separate from behavior changes. Evaluate configuration, foundations, runtime or backend, authentication, UI, dependencies, generated artifacts, and incidental fixes as distinct concerns rather than one capability chain.
- Keep tests and documentation with the behavior they verify or explain. Order foundations before consumers.
- Combine concerns only when splitting them would leave an earlier commit incoherent or broken, and state that constraint in the plan.

A large or cross-cutting diff should normally produce multiple commits. If the plan contains only one commit, explicitly explain before staging why every changed part has the same review concern and revert boundary and why no smaller coherent split exists. Never target a commit count based on lines changed or number of files.

Stage explicit paths or hunks for one planned group at a time and inspect the complete staged diff before each commit. Exclude secrets, generated noise, unrelated files, and unauthorized changes. Run appropriate validation and never bypass hooks.

Follow repository commit conventions; if none exist, use Conventional Commits and the user's language. Report the resulting commits, validation, and authorized changes left uncommitted.

Do not push or rewrite history unless explicitly requested.

Respond in the user's language unless the user requests otherwise.
