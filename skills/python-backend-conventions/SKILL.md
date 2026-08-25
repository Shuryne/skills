---
name: python-backend-conventions
description: Build or review Python backend services that intentionally use uv, FastAPI, Pydantic v2, pydantic-settings, Loguru, Scalar, Ruff, and pytest. Use for greenfield services adopting this stack or repositories that already use it; do not impose the stack on an unrelated existing project without an explicit migration request.
---

# Python Backend Conventions

Use this opinionated stack to make Python services predictable without forcing every project into the same architecture.

## When to use

Apply these conventions to a new service when the user chooses this stack, or to an existing repository that already uses it. In an existing project, read its instructions, `pyproject.toml`, nearby modules, tests, and documented decisions first. Preserve coherent local structure unless the user explicitly requests a migration.

Use the Python version declared by the project. For a new project, choose a currently supported version compatible with its dependencies instead of hard-coding a version in this skill.

## Stack

| Concern | Default |
| --- | --- |
| Dependency and command runner | uv |
| HTTP framework | FastAPI |
| Validation and serialization | Pydantic v2 |
| Runtime configuration | pydantic-settings |
| Application logging | Loguru |
| Interactive API documentation | Scalar |
| Formatting and linting | Ruff |
| Testing | pytest |

Use project scripts when they exist. Otherwise, these commands are the baseline:

```bash
uv add fastapi pydantic pydantic-settings loguru scalar-fastapi
uv add --dev ruff pytest
uv run fastapi dev
uv run ruff format .
uv run ruff check .
uv run pytest
```

Confirm package names and commands against the installed versions and project configuration rather than copying the baseline blindly.

## Project shape

A service with several resources and real business logic can use this shape:

```text
app/
├── main.py
├── api/
├── schemas/
├── services/
├── repositories/
└── core/
tests/
```

This is a scaling guide, not a required scaffold. Keep a small service flat until separation reduces real complexity. Introduce a boundary when logic is shared, changes for a different reason, needs an independent test seam, or hides infrastructure details from the rest of the application.

- **HTTP handlers** parse and validate input, apply authentication and transport concerns, call application behavior, and translate the result into the declared response.
- **Business logic** owns decisions and invariants without depending on FastAPI request or response objects.
- **Data access** owns persistence queries and mapping without deciding HTTP status codes or formatting client errors.

Avoid layers that only forward identical arguments and return values. Prefer one obvious path through the system over parallel patterns for the same responsibility.

## Configuration

Define runtime configuration with `BaseSettings` and create it in one place. A typical pattern is:

```python
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    log_level: str = "INFO"


@lru_cache
def get_settings() -> Settings:
    return Settings()
```

Adapt loading and caching to the application's lifecycle and test strategy. Keep `.env.example` synchronized with public configuration keys, make missing required values fail clearly, and inject or override settings cleanly in tests.

Environment variables are for deployment-varying values such as URLs, credentials, feature flags, and operational settings. Stable algorithm choices and domain constants belong in code. Do not scatter direct environment reads across modules.

Never commit secrets, place production-like credentials in defaults, expose secret values through model serialization, or include them in logs and error responses.

## API contracts and errors

Use named Pydantic models for non-trivial request and response bodies. Declare `response_model` and the intended status code so runtime behavior, generated OpenAPI, and tests share one contract. Use Pydantic constraints for real input rules, not validation duplicated manually in handlers.

Persistence models are internal. Map them to response models explicitly or through a deliberate Pydantic configuration such as `from_attributes=True`; do not let database-only fields leak into the public API.

Choose response envelopes, pagination, error shapes, and route versioning at the project level. Apply each decision consistently across endpoints. Use semantic HTTP status codes rather than returning successful responses that contain embedded failures.

Represent expected application failures with stable application exceptions or result types, then translate them to HTTP responses in a centralized handler or a small transport adapter. Keep unexpected exception details out of client responses while preserving enough context in logs for diagnosis.

Write OpenAPI summaries, descriptions, constraints, and examples when they help a consumer understand or exercise the contract. Mount Scalar at the project-selected documentation route and keep it aligned with the same OpenAPI schema. Do not add repetitive descriptions solely to fill every available field.

## Async and logging

Use `async def` only when the request path awaits non-blocking operations. Do not call synchronous database, filesystem, network, or CPU-heavy work directly from an async handler; use a synchronous handler, an async-compatible dependency, a thread boundary, or a worker according to the workload.

Configure Loguru once at application startup. Bind useful context such as request, correlation, resource, or job identifiers instead of constructing inconsistent message strings across modules. Integrate framework and server logs when it improves observability, but keep sink, rotation, retention, and serialization choices appropriate to the deployment environment.

Log meaningful state changes and failures. Do not log credentials, tokens, sensitive payloads, or complete request bodies by default.

## Testing

Use pytest to verify observable behavior through stable interfaces:

- HTTP contract tests cover validation, response models, status codes, authentication, and error translation.
- Business tests cover domain rules without requiring an HTTP server.
- Integration tests cover important persistence or external-service boundaries with controlled dependencies.
- Regression tests reproduce a reported failure before proving the fix.

Use FastAPI's `TestClient` for synchronous tests or an HTTPX async client when the application and fixtures are asynchronous. Override dependencies explicitly and keep expected values independent from the implementation being tested.

## Completion checklist

Before finishing a change:

- dependency declarations and the uv lockfile are synchronized;
- `uv run ruff format .` and `uv run ruff check .` pass, or repository-equivalent commands have been run;
- `uv run pytest` passes at the scope justified by the change;
- configuration examples, OpenAPI documentation, tests, and implementation describe the same behavior;
- no secrets, blocking work on async paths, undeclared response shapes, or persistence-only fields cross a public boundary;
- skipped checks and remaining risks are reported.
