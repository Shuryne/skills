# CLAUDE.md

## What this repo is

A personal skills repository, published as a Claude Code plugin marketplace. Each skill captures a
development habit so a new project does not require re-teaching the same conventions.

The skills are written for Claude Code first; the plain-markdown SKILL.md files are also readable by
Codex or any other agent by pointing it at `skills/<name>/SKILL.md`.

## Layout

```
.
├── .claude-plugin/
│   ├── marketplace.json     # marketplace catalog — one plugin: dev-skills, source "./"
│   └── plugin.json          # plugin manifest (repo root is the plugin)
├── skills/
│   └── <skill-name>/SKILL.md
└── CLAUDE.md
```

Repo root doubles as both marketplace and plugin, so a single `/plugin marketplace add` installs
everything.

## Installing / testing locally

```bash
# in Claude Code
/plugin marketplace add ~/work/skills
/plugin install dev-skills@shuryne-skills
/reload-plugins
```

After publishing to GitHub, others use `/plugin marketplace add shuryne/skills`.
Bump `version` in **both** `.claude-plugin/plugin.json` and the marketplace entry on every release —
without a bump, installed copies do not update.

## Rules for authoring skills here

- One skill = one `SKILL.md`. No `reference/` files unless a skill genuinely outgrows a single
  document — extra files are a last resort, not the default.
- Skill content is written in **English**, even when the conventions it describes require Chinese
  output (e.g. Chinese API descriptions).
- Directory name == frontmatter `name`: lowercase, hyphens, no `claude`/`anthropic`.
- Frontmatter has exactly `name` and `description`. The `description` states what the skill does
  **and when to use it**, in third person — it is the only thing loaded at startup, so it decides
  whether the skill triggers.
- **Principles, not code dumps.** State the rule; add a short snippet only where the shape of the
  rule is hard to convey in words. Long, complete code samples make agents copy verbatim and hurt
  generalization to a different project.
- Be prescriptive: one way to do a thing, no menus of alternatives. Prefer tables and checklists.
- No time-sensitive statements and no pinned library versions that will go stale.
- Assume the reader is a competent engineer — document only what is specific to these conventions.

## Skills

| Skill                                            | Covers                                                    |
| ------------------------------------------------ | --------------------------------------------------------- |
| [python-backend](skills/python-backend/SKILL.md) | uv + Python 3.13 + FastAPI + Loguru + Scalar conventions  |
| [git-commit](skills/git-commit/SKILL.md)         | Atomic commits that follow repository conventions                  |

## Cross-cutting preferences (apply to future skills too)

- **Consistency above all**: the codebase must read as if written by one person from one set of
  principles. Never introduce a second way of doing something that already has a way.
- Sparse, short comments — only where the *why* is non-obvious.
- Mechanically derived naming for files, directories, functions and types.
- API request/response types are always named `<Verb><Resource>Request` / `<Resource>Response`.
