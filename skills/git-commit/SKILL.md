---
name: git-commit
description: Create atomic Git commits from authorized local changes while following the repository's established conventions. Use only when the user explicitly asks to commit changes; do not use merely because a task has finished.
---

# Git Commit

Create Git commits from the authorized local changes.

Follow the repository's established commit conventions, including its message format and language. If no clear convention exists, use Conventional Commits and the user's language.

Organize changes into atomic commits. Each commit should represent one coherent purpose, include its related code, tests, configuration, and documentation, and remain independently understandable and revertible without leaving the repository incoherent. Keep unrelated changes in separate commits.

Respond in the user's language unless the user requests otherwise.
