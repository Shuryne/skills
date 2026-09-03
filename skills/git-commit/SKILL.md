---
name: git-commit
description: Plan and create reviewable atomic Git commits from authorized local changes while following repository conventions. Use only when the user explicitly asks to commit changes; do not use merely because a task has finished.
---

# Git Commit

Inspect all authorized staged, unstaged, and untracked changes before staging. Read repository guidance and recent commits for the established message format and language. Preserve unrelated work and treat the existing index as user state.

Before mutating the index, present an ordered commit plan with each group's intent, paths or hunks, and dependencies. Proceed without waiting unless the grouping is genuinely ambiguous, risky, or would alter already-staged user state.

Use reviewability, coherent intent, and practical revert boundaries to choose groups:

- Each commit should have one understandable purpose. A commit may depend on earlier commits in the same series and does not need to deliver a complete standalone feature.
- Prefer separating changes with different reviewer concerns or reasons to revert, but keep tightly coupled changes together when splitting would create misleading intermediate states, temporary scaffolding, or unnecessary validation failures.
- Separate structural changes from behavior changes when the structural change remains meaningful and verifiable on its own. Otherwise, commit them together.
- Keep tests and documentation with the behavior they verify or explain. Order foundations before consumers.
- Avoid introducing unnecessary breakage between commits. Preserve build and test integrity at every commit when practical or when the repository explicitly requires bisectable history.

A large or cross-cutting diff should normally produce multiple commits. Use a single commit when the changes form one tightly coupled review unit, and briefly state that reasoning in the plan. Never target a commit count based on lines changed or number of files.

Stage explicit paths or hunks for one planned group at a time and inspect the complete staged diff before each commit. Exclude secrets, generated noise, unrelated files, and unauthorized changes. Run appropriate validation and never bypass hooks.

Follow repository commit conventions; if none exist, use Conventional Commits and the user's language. Report the resulting commits, validation, and authorized changes left uncommitted.

Do not push or rewrite history unless explicitly requested.

Respond in the user's language unless the user requests otherwise.
