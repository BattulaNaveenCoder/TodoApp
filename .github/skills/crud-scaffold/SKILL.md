---
name: crud-scaffold
description: "Scaffold a complete CRUD feature for a new entity across the full stack. Creates SQLAlchemy model, Pydantic schemas, repository, service, router (backend) and TypeScript types, API service, React Query hooks, components, and page (frontend). Use when adding a new domain entity like Category, Tag, or any new resource."
argument-hint: "[entity name] [fields description]"
---

# CRUD Scaffold Skill

Scaffold a new CRUD entity end-to-end across the 3-layer backend and React frontend.

## Architecture Rules

- **3-layer backend**: Route → Service → Repository. No layer may skip another.
- **DI flow**: `get_db()` → Repository(db) → Service(repo) → Route(service)
- **commit()** happens automatically via the `get_db()` context manager in session.py.
- **All code is async**: `async def`, `AsyncSession`, `create_async_engine`.

## Backend Files to Create (in order)

1. `api/app/models/{entity}.py` — SQLAlchemy ORM model using `mapped_column`, `Mapped` type hints
2. `api/app/models/__init__.py` — Add import for the new model (after `Base` definition)
3. `api/app/schemas/{entity}.py` — Pydantic v2 DTOs: `{Entity}Create`, `{Entity}Update`, `{Entity}Response` with `ConfigDict(from_attributes=True)`
4. `api/app/repositories/{entity}_repository.py` — All DB queries: `get_all`, `get_by_id`, `create`, `update`, `delete`
5. `api/app/services/{entity}_service.py` — Business logic, raises `HTTPException` for 404/409
6. `api/app/routes/{entity}_router.py` — FastAPI router with DI, 5 CRUD endpoints
7. `api/app/main.py` — Register the new router via `include_router`
8. `api/alembic/versions/` — Migration file for the new table

## Frontend Files to Create (in order)

1. `web/src/types/{entity}.ts` — TypeScript interfaces matching Pydantic schemas
2. `web/src/services/{entity}Service.ts` — Axios CRUD functions using the shared `api` instance
3. `web/src/hooks/use{Entities}.ts` — React Query hooks: `use{Entities}`, `useCreate{Entity}`, `useUpdate{Entity}`, `useDelete{Entity}`
4. `web/src/components/{Entity}Form.tsx` — Form component for creating new items
5. `web/src/components/{Entity}Item.tsx` — Single item display with actions
6. `web/src/components/{Entity}List.tsx` — List component with loading/error/empty states
7. `web/src/pages/{Entity}Page.tsx` — Page composing form + list

## Coding Standards

### Python
- All functions have type hints and docstrings
- Use `logging` module, never `print()`
- snake_case for functions/variables, PascalCase for classes
- One model per file, one schema set per file

### TypeScript
- Functional components with explicit types
- Named exports (except page components which use default export)
- camelCase for functions/variables, PascalCase for components/types
- Use the shared Axios instance from `src/services/api.ts`

## HTTP Status Codes
- GET: 200
- POST: 201
- PATCH: 200
- DELETE: 204
- Not Found: 404
- Conflict: 409
- Validation Error: 422
