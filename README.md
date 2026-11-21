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
| [`fastapi`](skills/fastapi/SKILL.md) | Automatic or explicit | Apply official FastAPI guidance for routing, dependencies, response models, and streaming. |
| [`frontend-design`](skills/frontend-design/SKILL.md) | Automatic or explicit | Establish a visual direction and design new or existing interfaces around the product and its audience. |
| [`git-commit`](skills/git-commit/SKILL.md) | Explicit only | Create atomic commits that follow repository conventions. |
| [`supabase-postgres-best-practices`](skills/supabase-postgres-best-practices/SKILL.md) | Automatic or explicit | Apply Supabase guidance to PostgreSQL schema, migrations, SQL, security, and performance. |
| [`vercel-react-best-practices`](skills/vercel-react-best-practices/SKILL.md) | Automatic or explicit | Apply Vercel performance guidance to React and Next.js code. |
| [`web-design-guidelines`](skills/web-design-guidelines/SKILL.md) | Automatic or explicit | Review UI code against Vercel’s Web Interface Guidelines. |

In Codex, invoke a skill explicitly with `$skill-name`. Claude Code exposes installed skills through its plugin commands and skill picker. Automatic invocation depends on the skill description and its platform-specific policy.

`vercel-react-best-practices` is adapted from Vercel's [upstream snapshot at `dc8367e`](https://github.com/vercel-labs/agent-skills/tree/dc8367e6f91c022d83361f03c3313fa05e848ee5/skills/react-best-practices).

`fastapi` is an unmodified upstream snapshot from [FastAPI release `0.165.0`](https://github.com/fastapi/fastapi/releases/tag/0.165.0), at commit [`05e6df7e906c3decba377c37548019973f40bf15`](https://github.com/fastapi/fastapi/tree/05e6df7e906c3decba377c37548019973f40bf15/fastapi/.agents/skills/fastapi). To update it, compare the skill directory at the recorded commit with the target release, then copy the full directory and update this pin.

`frontend-design` is adapted from Anthropic's [upstream snapshot at `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`](https://github.com/anthropics/skills/tree/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/frontend-design). The local copy moves the license reference out of the frontmatter. To update it, compare the upstream skill directory at the recorded and target commits, reapply that change, retain the upstream license, and update this pin.

`supabase-postgres-best-practices` is adapted from Supabase's [upstream snapshot at `c9be0e931b7930f7d02126d04774d904c381e7d7`](https://github.com/supabase/agent-skills/tree/c9be0e931b7930f7d02126d04774d904c381e7d7/skills/supabase-postgres-best-practices). The local copy adapts the entrypoint and retains the upstream rule references. To update it, compare the pinned and target directories, sync the rule references, review the entrypoint and license, and update this pin.

## License

The repository uses the [MIT License](LICENSE) by default. `vercel-react-best-practices` and `web-design-guidelines` are adapted from [Vercel’s Agent Skills](https://github.com/vercel-labs/agent-skills). The official [FastAPI skill](https://github.com/fastapi/fastapi/tree/05e6df7e906c3decba377c37548019973f40bf15/fastapi/.agents/skills/fastapi) is also licensed under MIT. Anthropic's `frontend-design` skill is licensed under [Apache 2.0](skills/frontend-design/LICENSE.txt).

Supabase's `supabase-postgres-best-practices` skill retains its [upstream MIT license](skills/supabase-postgres-best-practices/LICENSE).
