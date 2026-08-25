---
name: python-backend-conventions
description: Build or review Python backend services that intentionally use uv, FastAPI, Pydantic v2, pydantic-settings, Loguru, Scalar, Ruff, and pytest. Use for greenfield services adopting this stack or repositories that already use it; do not impose the stack on an unrelated existing project without an explicit migration request.
---

# Python Backend Conventions

Use the project's declared Python version and established structure. Apply this stack to new services that choose it or existing repositories that already use it; do not migrate unrelated projects unless the user explicitly requests it.

## Stack

- Dependency and command runner: uv
- HTTP framework: FastAPI
- Validation and serialization: Pydantic v2
- Runtime configuration: pydantic-settings
- Application logging: Loguru
- Interactive API documentation: Scalar
- Formatting and linting: Ruff
- Testing: pytest

## Core conventions

- Keep architecture proportional to the service. Separate HTTP, business, and data-access responsibilities when it reduces real complexity; avoid pass-through layers.
- Centralize runtime configuration with `BaseSettings` and logging setup with Loguru. Keep configuration examples synchronized and never expose secrets.
- Use named Pydantic models for non-trivial API contracts. Declare response models and status codes, keep persistence models internal, and apply response, error, and documentation conventions consistently.
- Use `async` only for non-blocking work and keep blocking operations off the event loop.
- Test observable behavior with pytest and finish with the repository's Ruff and pytest commands, using uv when no project scripts exist.

Respond in the user's language unless the user requests otherwise.
