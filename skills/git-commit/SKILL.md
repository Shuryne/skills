---
name: git-commit
description: Plans logical Git commit batches and creates them when explicitly requested. Use when the user asks for a commit plan or to commit local changes.
---

# Git Commit

Inspect staged, unstaged, and untracked changes within the user's scope.

Split the work into small, independently reviewable commits. Give each
commit one clear purpose and order the commits by dependency. Keep tests
and documentation with the changes they cover.

Before staging, present a concise, ordered plan with the scope and proposed
message for each commit. Follow the repository's commit message conventions.
If none exist, use Conventional Commits and write in the user's language.

When explicitly asked to commit, stage one planned batch at a time, review
the staged diff, and run relevant checks. Preserve unrelated work and
existing staging outside the authorized scope. Do not bypass hooks.
Report the commits, validation, and any authorized changes left uncommitted.
Push or rewrite history only when explicitly requested.
