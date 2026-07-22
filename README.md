# skills

Personal development-convention skills for [Claude Code](https://code.claude.com), packaged as a
plugin marketplace. Install once and every project starts with the same habits instead of
re-teaching an agent from scratch.

## Install

```bash
/plugin marketplace add shuryne/skills
/plugin install dev-skills@shuryne-skills
/reload-plugins
```

Local development:

```bash
/plugin marketplace add ~/work/skills
```

## Skills

| Skill                                            | What it does                                                                                |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| [python-backend](skills/python-backend/SKILL.md) | Python backend conventions: uv + Python 3.13 + FastAPI + Loguru + Scalar, naming rules, bilingual OpenAPI docs, daily-rotated logs |
| [git-commit](skills/git-commit/SKILL.md)         | Atomic commit splitting and Conventional-Commits messages with Chinese subjects and why-focused bodies |
| [codebase-cleanup](skills/codebase-cleanup/SKILL.md) | Periodic behavior-preserving cleanup: audit for duplication, inconsistency and doc drift, plan for approval, then execute |

Each skill triggers automatically when the task matches its description, or can be invoked directly
as `/dev-skills:<skill-name>`.

## Using without Claude Code

The skills are plain markdown. Point any agent at `skills/<name>/SKILL.md` — for Codex, referencing
the file (or copying it into `AGENTS.md`) works the same way.

## License

MIT
