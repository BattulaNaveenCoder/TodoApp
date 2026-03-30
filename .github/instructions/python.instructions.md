---
description: "Use when writing Python backend code. Covers FastAPI, SQLAlchemy async, and Pydantic v2 patterns."
applyTo: "api/**/*.py"
---

# Python / FastAPI Conventions

- Use `async def` for all route handlers, service methods, and repository methods.
- Use SQLAlchemy 2.x async API: `AsyncSession`, `select()`, `async_sessionmaker`.
- Pydantic v2: use `model_config = ConfigDict(from_attributes=True)`.
- Repository methods accept `db: AsyncSession` as the first parameter.
- Service methods accept a repository instance injected via `Depends()`.
- Route handlers accept a service instance injected via `Depends()`.
- Use Python 3.11+ syntax. Type-hint all function parameters and return values.
- Raise `HTTPException` with appropriate status codes (400, 404, 409, 422).
- Use the `logging` module, never `print()`.
- Imports: stdlib → third-party → local, separated by blank lines.
- One model per file in `app/models/`, one schema set per file in `app/schemas/`.
