---
name: git-commit
description: Inspect pending repository changes, split them into coherent units, and create safe Git commits that follow the repository's conventions. Use only when the user explicitly invokes this skill to commit or reorganize local work; do not use merely because a task has finished.
---

# Git Commit

Turn authorized local changes into reviewable commits without absorbing unrelated work or changing remote history.

## 1. Inspect

Build the complete picture before staging or committing:

- Run `git status --short` to identify staged, unstaged, and untracked paths.
- Read both `git diff` and `git diff --staged`; neither view alone represents the whole working tree.
- Inspect relevant untracked files without assuming they belong in the commit.
- Read recent commit subjects and repository guidance such as `CONTRIBUTING.md` to learn the established message format and language.
- Identify the changes authorized by the user's request and distinguish pre-existing work from changes created for the current task.

Treat the existing index as user state. Record what was already staged and do not unstage, replace, or regroup it without explaining why and obtaining confirmation when that would change the user's intended commit.

## 2. Build commit groups

Each commit should express one coherent purpose that a reviewer can understand and revert independently. Use these tests:

- **Cohesion**: code, tests, configuration, and documentation that jointly complete one behavior belong together.
- **Independence**: unrelated fixes, mechanical formatting, dependency updates, and generated artifacts usually belong in separate commits.
- **Dependency order**: foundations such as shared types or configuration precede the changes that consume them.
- **Intermediate integrity**: a split is invalid if an earlier commit leaves the repository incoherent or unnecessarily broken.

For example, an endpoint and its contract tests normally stay together; a drive-by typo in another module does not. A file move may be separate from a behavior change when that improves reviewability, but not when the intermediate state would break imports or obscure the actual change.

When several groupings are equally reasonable, or when regrouping touches changes that were already staged, present the proposed commit sequence before mutating the index.

## 3. Stage safely

Stage explicit paths when a whole file belongs to one group. Use hunk staging when one file contains independent changes. Before every commit, inspect `git diff --staged --stat` and the full staged diff, then confirm that it matches exactly one planned group.

Exclude secrets, `.env` files, credentials, local configuration, logs, temporary files, unrelated build output, and unrequested user changes. Do not use broad staging merely for convenience when the working tree contains mixed work.

## 4. Write the message

Follow the repository's established message format and language. If no clear convention exists, use Conventional Commits:

```text
<type>(<optional-scope>): <concise imperative subject>

<optional body explaining motivation, constraints, or tradeoffs>
```

Good examples:

```text
fix(auth): preserve refresh tokens during rotation

The previous flow revoked the token before the replacement was persisted, leaving retrying clients unable to recover.
```

```text
docs: align local setup with the uv workflow
```

Use a body when the reason is not obvious from the subject or diff. Explain why the change exists, important constraints, and intentionally deferred work; do not narrate changed files line by line.

## 5. Validate and commit

Run validation appropriate to the group before committing. Prefer the repository's documented commands and targeted checks that exercise the changed behavior.

Allow hooks to run. If a hook fails, address the cause when it is within scope or report the blocker; do not bypass it with `--no-verify`. If a hook modifies files, reinspect the working tree and staged diff before retrying so generated fixes do not absorb unrelated work.

After each commit, record its short SHA and subject. At the end, report the commit sequence, validation performed, and any authorized changes left uncommitted.

Do not push, amend published commits, rebase, reset, or otherwise rewrite existing history unless the user explicitly requests that separate operation and the affected history is safe to rewrite.
