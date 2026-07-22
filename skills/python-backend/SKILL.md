---
name: python-backend
description: Builds Python backend services with uv, Python 3.13, FastAPI, Loguru and Scalar, following fixed conventions for project layout, naming, configuration, API responses, bilingual OpenAPI documentation and logging. Use when starting a new Python backend, adding or changing FastAPI endpoints, wiring configuration or logging, or reviewing Python service code for consistency.
---

# Python Backend Conventions

## Stack

| Concern     | Choice                                                    |
| ----------- | --------------------------------------------------------- |
| Package     | `uv` only — never `pip`, never manual venv activation      |
| Runtime     | Python 3.13 (`requires-python = ">=3.13"`)                 |
| Framework   | FastAPI + Pydantic v2 + pydantic-settings                  |
| Logging     | Loguru                                                     |
| API docs    | Scalar at `/scalar`; Swagger UI and ReDoc disabled         |
| Lint/format | Ruff                                                       |

Everything runs through `uv`: `uv add <pkg>`, `uv sync`, `uv run uvicorn app.main:app --reload`,
`uv run ruff format . && uv run ruff check --fix .`, `uv run pytest`.

## The rule above all: consistency

The codebase must read as if one person wrote it from one set of principles. Before adding
anything, read the nearest existing sibling and follow it exactly. Never introduce a second way of
doing something that already has a way — if a change would create an inconsistency, either update
every existing occurrence too, or don't make the change.

These hold across **every** endpoint and module, with no exceptions:

- Every endpoint follows the same response and error convention — one shape, no per-endpoint variation.
- Every request/response body is a named Pydantic model, never an inline `dict`.
- Every endpoint has an English `summary` and English `tags`, and a Chinese `description`.
- Every model field has a Chinese `description`; every model carries a realistic example.
- Errors are raised as one application exception type and converted by one global handler.
- Layer boundaries are never skipped: router → service → repository.

## Layout

`app/` at the repository root (no `src/` layer, so `uv run uvicorn app.main:app` needs no packaging
config). One module per resource in each layer, same stem across layers.

```
app/
├── main.py          # create_app(): settings, logging, middleware, handlers, routers, Scalar mount
├── core/            # config, logging, exceptions, middleware
├── api/             # routers, one module per resource
├── schemas/         # request/response models
├── services/        # business logic
├── repositories/    # data access
└── models/          # persistence models
tests/
logs/                # runtime output, gitignored
```

Layer contracts:

- Routers declare and wire only — validate via Pydantic, call one service function, return its
  result. No business logic, no error formatting.
- Services own business rules, raise the application exception, and return schema models
  (ORM → response model conversion happens here, not in the router).
- Repositories do data access only: no business rules, no application exceptions, return
  persistence models or primitives.
- Routers are registered in exactly one aggregation module; nothing else includes routers.
- Routes are mounted under `/api` with **no version segment** — `/api/users`, not `/api/v1/users`.
  Versioning is added only if a real breaking change ever forces it, not preemptively.

## Configuration

One `Settings` object from pydantic-settings, imported as `settings`. `os.getenv` appears nowhere
else in the codebase.

- **Environment-dependent settings carry no default value** — host, port, log level, log directory,
  database URL, external endpoints, credentials. Declare them as required fields so a missing key
  fails at startup instead of silently running on a fallback that differs between machines.
- Everything the service reads comes from `.env`; `.env.example` lists every key with a placeholder
  and is updated in the same change that adds a setting.
- `.env` is gitignored. Secrets never get a default, never get committed, and never appear in logs.
- Defaults are acceptable only for values that are part of the code, not the environment (e.g. a
  page-size cap) — and those belong in the code as constants, not in settings.

## Naming

Derive names mechanically from the resource name — never improvise.

| Thing               | Rule                          | Example for `order_item`             |
| ------------------- | ----------------------------- | ------------------------------------ |
| Files / dirs        | `snake_case`, no abbreviations| `order_item_service.py`              |
| Route module        | plural resource               | `api/order_items.py`                 |
| Other layer modules | singular resource             | `schemas/order_item.py`              |
| Route path          | plural, lowercase, hyphenated | `/api/order-items`                   |
| Tag                 | English PascalCase plural     | `OrderItems`                         |
| Request model       | `<Verb><Resource>Request`     | `CreateOrderItemRequest`             |
| Query model         | `List<Resource>Request`       | `ListOrderItemsRequest`              |
| Response model      | `<Resource>Response`          | `OrderItemResponse`                  |
| Action response     | `<Verb><Resource>Response`    | `LoginResponse`                      |
| Service function    | `verb_noun`, async            | `create_order_item`                  |
| Repository function | `verb_by_field`               | `get_by_id`, `list_paged`            |

Never reuse a request model as a response model, and never expose persistence models directly.

## API contract

The response shape is a project-level decision, made once and then never varied. Pick the shape that
fits the consumer — plain response models with semantic HTTP status by default, or a wrapper
envelope when the frontend or gateway needs business codes. Whichever is chosen, it is written down
and applied to **every** endpoint. Half the API returning a wrapper and half returning bare payloads
is the exact inconsistency to avoid.

Defaults when nothing argues otherwise:

- Return the response model directly, `response_model=XxxResponse`, and let HTTP status carry the
  outcome — `201` on create, `204` on delete, `4xx`/`5xx` on failure. Never return 200 for a failure.
- Lists are paginated with a shared page-query base (`page`, `page_size`) and a generic page payload
  carrying `items` / `page` / `page_size` / `total`.
- If the project does use business codes, they live in one `IntEnum` and nowhere else, and the code →
  HTTP status mapping is derivable rather than a lookup table.

Errors flow one way only — services raise a single application exception, global handlers translate
it into the project's error shape:

```python
raise AppError(ErrorCode.CONFLICT, "邮箱已被注册")
```

Handlers cover the application exception, request-validation errors, and unexpected exceptions
(logged with `logger.exception`, returned as a generic 500 message that leaks no internals). Routers
never catch or format errors, and the error body shape is identical across all three handlers.

## OpenAPI / Scalar documentation

The goal: any endpoint can be understood and test-fired from Scalar without reading the code.

- `summary`: English, imperative, short — `"Create user"`.
- `tags`: English, one per resource, set on the router; described once in `openapi_tags` with an
  English name and a Chinese description.
- `description`: Chinese — what it does, business rules, side effects, notable error codes.
- Field `description`: Chinese, on every field of every request and response model, together with
  validation constraints (`min_length`, `ge`, `max_length`, …).
- Example: every model sets one realistic example via `model_config`, so Scalar's test request works
  with a single click. Path and query parameters get Chinese descriptions and examples too.

```python
class CreateUserRequest(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={"example": {"email": "zhangsan@example.com", "nickname": "张三"}}
    )

    email: EmailStr = Field(description="用户邮箱，全局唯一，作为登录账号")
    nickname: str = Field(min_length=1, max_length=32, description="用户昵称")


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create user",
    description="创建一个新用户。邮箱全局唯一，重复时返回 409；密码加密后存储。",
)
async def create_user(payload: CreateUserRequest) -> UserResponse:
    return await user_service.create_user(payload)
```

## Logging

Loguru only — no `logging`, no `print`, no per-module logger. Import `from loguru import logger`
everywhere; configure once at startup.

- File sink `logs/{time:YYYY-MM-DD}.log` with `rotation="00:00"` and `retention="14 days"`,
  `encoding="utf-8"`, `enqueue=True`. Plain `.log`, no compression — files stay greppable.
- Console sink in development; one shared format string for both sinks.
- Intercept stdlib and uvicorn logging into Loguru so all output has one format.
- One middleware logs each request once — method, path, status, duration — and binds a request id
  that appears in every log emitted while handling that request.

```python
logger.add(
    settings.log_dir / "{time:YYYY-MM-DD}.log",
    level=settings.log_level,
    format=LOG_FORMAT,
    rotation="00:00",
    retention="14 days",
    encoding="utf-8",
    enqueue=True,
)
```

| Level     | Use for                                                             |
| --------- | ------------------------------------------------------------------- |
| `DEBUG`   | Local troubleshooting detail; off in production                      |
| `INFO`    | State changes worth an audit trail: created, updated, deleted, sent  |
| `WARNING` | Expected failures: business errors, retries, degraded fallbacks      |
| `ERROR`   | Unexpected failures needing a human; use `logger.exception`          |

Messages are Chinese, followed by `|`-separated key values:
`logger.info(f"创建用户成功 | id={user.id} email={user.email}")`. One log per meaningful action —
not entry/exit of every function. Never log passwords, tokens, or whole request bodies.

## Code style

- Comments are rare and short: one line, Chinese, only when the *why* is not obvious — business
  rules, non-obvious ordering, workarounds. Never restate what the code does. No banner comments.
- No docstrings on routers, schemas or trivial functions; the OpenAPI `description` is the documentation.
- Full type hints, modern syntax (`str | None`, `list[str]`) — no `typing.Optional` / `List`.
- `async def` on I/O paths; keep blocking work off the event loop.
- Small modules: split by sub-domain before a service module gets unwieldy.
- No dead code, no commented-out code.

## Before finishing

1. Names derived mechanically from the resource name?
2. Touched endpoints: same response convention as their siblings, English summary/tags, Chinese
   description, example present?
3. New fields: Chinese `description` and constraints?
4. Errors raised as the application exception, not built ad hoc?
5. New settings: no default value, added to `.env.example`, read only through `settings`?
6. Meaningful actions logged at the right level, nothing sensitive logged?
7. `uv run ruff format . && uv run ruff check --fix .` clean?
8. Would a reader guess this file was written by the same person as its siblings?
