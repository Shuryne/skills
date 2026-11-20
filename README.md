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

## Skills

| Skill | Invocation | Purpose |
| --- | --- | --- |
| [`codebase-cleanup`](skills/codebase-cleanup/SKILL.md) | Automatic or explicit | Review and improve code and documentation, proposing a complete plan before editing. |
| [`git-commit`](skills/git-commit/SKILL.md) | Explicit only | Create atomic commits that follow repository conventions. |
| [`python-backend-conventions`](skills/python-backend-conventions/SKILL.md) | Automatic or explicit | Build consistent services with uv, FastAPI, Pydantic, Loguru, Scalar, Ruff, and pytest. |
| [`vercel-react-best-practices`](skills/vercel-react-best-practices/SKILL.md) | Automatic or explicit | Apply Vercel performance guidance to React and Next.js code. |
| [`web-design-guidelines`](skills/web-design-guidelines/SKILL.md) | Automatic or explicit | Review UI code against Vercel’s Web Interface Guidelines. |

In Codex, invoke a skill explicitly with `$skill-name`. Claude Code exposes installed skills through its plugin commands and skill picker. Automatic invocation depends on the skill description and its platform-specific policy.

`vercel-react-best-practices` is adapted from Vercel's [upstream snapshot at `dc8367e`](https://github.com/vercel-labs/agent-skills/tree/dc8367e6f91c022d83361f03c3313fa05e848ee5/skills/react-best-practices).

## License

The repository is licensed under the [MIT License](LICENSE). The two frontend skills are adapted from [Vercel’s Agent Skills](https://github.com/vercel-labs/agent-skills), also licensed under MIT.
