# TodoApp — Copilot Instructions

## Architecture

This is a monorepo with `/api` (Python FastAPI backend) and `/web` (React TypeScript Vite frontend).

The backend uses a strict **3-layer architecture**:

1. **Routes** (`app/routes/`) — FastAPI routers. Validate input via Pydantic, delegate to Service, return HTTP responses. No business logic. No DB access.
2. **Services** (`app/services/`) — All business rules. Call Repository layer. Raise `HTTPException` for violations. No SQLAlchemy queries.
3. **Repositories** (`app/repositories/`) — All SQLAlchemy queries. Accept `AsyncSession` via DI. Return ORM model objects. No business logic. No HTTP knowledge.

**Dependency injection flow:**
```
get_db() → Repository(db) → Service(repo) → Route(service)
```

## Coding Standards

- All backend code is **async** (`async def`, `AsyncSession`, `create_async_engine`).
- All functions must have **type hints** (Python) or **TypeScript types** (frontend).
- All public functions must have **docstrings** (Python) or **JSDoc** (TypeScript).
- Use **Pydantic v2** schemas for all API request/response DTOs. Never return raw ORM objects.
- `commit()` is called in the **Service layer**. Rollback is automatic via the `get_db()` context manager.
- Frontend uses **React Query** for server state and **Axios** for HTTP calls.
- Follow **conventional commits**: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`
- Never hardcode secrets. Use `.env` files.
- Use `logging` module, not `print()`.

## Naming Conventions

- Python: `snake_case` for functions/variables, `PascalCase` for classes.
- TypeScript: `camelCase` for functions/variables, `PascalCase` for components/types/interfaces.
- Files: `snake_case.py` for Python, `camelCase.ts` / `PascalCase.tsx` for TypeScript.
- API endpoints: `/todos`, `/todos/{id}`, `/categories` (plural, lowercase).

## Error Handling

- Return meaningful HTTP status codes: 200, 201, 204, 400, 404, 409, 422, 500.
- Always validate input with Pydantic schemas at the route level.
- Never expose internal error details to the client in production.
