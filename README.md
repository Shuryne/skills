# Shuryne Skills

Reusable engineering workflows for Claude Code, Codex, and other agents that support the Agent Skills format. The collection favors small, focused skills that preserve project context and user control.

## Install

### Codex

```bash
codex plugin marketplace add Shuryne/skills
codex plugin add shuryne-skills@shuryne
```

Restart Codex or open a new task after installing or upgrading so the current skill definitions are loaded.

### Claude Code

```text
/plugin marketplace add Shuryne/skills
/plugin install shuryne-skills@shuryne
/reload-plugins
```

For local development, add the repository root as the marketplace source.

## Upgrade from 0.2.x

Version 0.3.0 renames the plugin from `dev-skills` to `shuryne-skills` and the marketplace from `shuryne-skills` to `shuryne`. Remove the old installation and add the marketplace and plugin again with the commands above. The `python-backend` skill was also renamed to `python-backend-conventions`.

## Skills

| Skill | Invocation | Purpose |
| --- | --- | --- |
| [`codebase-cleanup`](skills/codebase-cleanup/SKILL.md) | Automatic or explicit | Audit code and documentation, propose a prioritized cleanup plan, and wait for approval before editing. |
| [`git-commit`](skills/git-commit/SKILL.md) | Explicit only | Inspect pending work and create safe, coherent commits that follow repository conventions. |
| [`python-backend-conventions`](skills/python-backend-conventions/SKILL.md) | Automatic or explicit | Build consistent services with uv, FastAPI, Pydantic, Loguru, Scalar, Ruff, and pytest. |

In Codex, invoke a skill explicitly with `$skill-name`. Claude Code exposes installed skills through its plugin commands and skill picker. Automatic invocation depends on the skill description and its platform-specific policy.

## License

The repository is licensed under the [MIT License](LICENSE).
