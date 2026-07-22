---
name: codebase-cleanup
description: Audits a codebase for duplication, inconsistency, convention drift and stale documentation, then proposes a plan for approval before making any behavior-preserving change. Use when asked to 整理代码 / 整理文档 / clean up, tidy, refactor for consistency, remove redundancy, or bring a drifted codebase back in line — not for new features, bug fixes, performance work or hardening.
---

# Codebase Cleanup

A periodic pass that pays down structural debt so later feature work and bug fixing start from a
clean base. Every change here is **behavior-preserving**: the codebase does the same thing
afterwards, only clearer and more consistent.

## Scope

Optional argument selects the area — `frontend`, `backend`, `docs`; default is everything.

In scope:

| Category      | Looks for                                                                          |
| ------------- | ---------------------------------------------------------------------------------- |
| Redundancy    | Duplicated implementations, copy-pasted blocks, dead code, unused exports, needless abstraction layers |
| Consistency   | Same problem solved two ways: naming, directory placement, error handling, logging, response shapes, parameter order, config access |
| Conventions   | Naming rules, comment style, code style, module organization, file granularity      |
| Docs & comments | Stale, wrong, duplicated or contradictory docs and comments; comments that restate the code |

Out of scope — when found, record it in the report and **do not act on it**:

- New features, behavior changes, bug fixes (report the bug, leave the code alone)
- Performance optimization, database schema or migration changes
- Robustness hardening: added validation, retries, timeouts, new error branches
- Dependency upgrades, public API or contract changes, config value changes

If cleanup seems impossible without one of these, stop and say so instead of quietly crossing the line.

## Workflow

### 1. Audit (read-only)

Nothing is modified in this phase.

- Require a clean working tree. Uncommitted work would get mixed into the cleanup commits and make
  every one of them unreviewable — ask for it to be committed or stashed first.
- Establish a baseline: does the build pass, do the tests pass? Record it. If there are no tests,
  say so in the plan and restrict the work to mechanically verifiable changes (renames, moves,
  deletions of provably unused code).
- Read broadly before judging: entry points, directory layout, then the modules in scope.
- Every finding needs evidence — `file:line`, and for duplication, all the locations involved.
  Never report an impression.

### 2. Plan (hard stop)

Present the plan and **wait for approval**. Do not start editing, not even the "obvious" items.

Group findings in execution order, one entry per intended commit:

```
### 1. 删除（低风险）
- [证据] app/utils/format.py:12-40 与 app/helpers/text.py:8-33 完全重复，后者无引用
  → 删除 app/helpers/text.py，2 处引用改指向 format.py

### 2. 重命名 / 移动（机械可验证）
### 3. 去重 / 抽取（结构性，风险最高）
### 4. 一致性对齐
### 5. 文档与注释同步
```

Each entry states: the evidence, the action, how many files it touches, and how it will be verified.
End the plan with a **发现但不处理** list — bugs, performance issues, missing tests — so nothing is
lost even though it is out of scope.

Keep a plan reviewable. On a large codebase, propose one focused batch rather than a sweep nobody
can check; note what is deferred to a next pass. The user may approve only part of the plan — treat
unapproved entries as out of scope.

### 3. Execute

- One plan entry = one atomic commit, committed as soon as that entry is done — not all edits first
  and a split afterwards. The plan already fixed the commit boundaries, and refactoring edits
  overlap inside files, so a later `git add -p` split cannot separate them and would produce
  intermediate commits that were never verified.
- Follow the repository's commit conventions; most of these are `refactor`, `chore` or `docs`,
  never `feat` or `fix`.
- Verify **before** each commit — build, tests, type check. If verification fails, fix it or discard
  that entry's edits (`git restore`); never commit a broken state and never carry it into the next entry.
- Do not push during execution. The history stays local and malleable so the whole pass can be
  reviewed, reworded or reset afterwards at no cost.
- **Tests are the contract, not the target.** Never edit an assertion to make refactored code pass.
  A test that only breaks because a symbol was renamed may be updated; anything else is a real
  regression.
- Docs and comments go last: earlier entries change the facts they describe.
- No opportunistic extras. Anything discovered mid-execution goes on the next-pass list.

### 4. Report

What was changed (commit by commit), what was skipped and why, and the deferred findings list.

## Judging consistency

When two ways of doing something exist, the target is decided in this order:

1. The project's convention skill or documented standard, if one applies.
2. Otherwise, the form that already dominates the repository — count, don't guess.
3. Never introduce a third form that neither the standard nor the repository uses. Cleanup converges
   the codebase; it does not add the author's personal preference as a new variant.

The bar for "done": a reader should not be able to tell which parts were written earlier or by whom.

## Area-specific attention

**Frontend**: duplicated components and hooks that differ only in props; state handled locally in
some places and in a store in others; styling split across conventions; `any` used as an escape
hatch; deep directories holding one file each.

**Backend**: layer boundaries crossed (route logic in the data layer and vice versa); the same
payload modelled twice; error handling and logging done differently per module; configuration read
directly from the environment instead of through the settings object; near-identical query helpers.

**Docs**: README instructions that no longer match the code; the same thing explained in three files;
comment blocks describing removed parameters; changelog-style narration left inside source files.

## Rules that hold throughout

1. Behavior does not change. If a change could alter observable behavior, it belongs to a different
   kind of work and is out of scope.
2. No edits before approval; approval covers only what was in the plan.
3. Every finding is backed by a file and line, never by an impression.
4. Delete rather than comment out. Version control is the archive.
5. Removing duplication is not always right — two similar blocks that evolve independently should
   stay separate. Say so instead of forcing a shared abstraction.
6. Stop and report rather than expand scope.
