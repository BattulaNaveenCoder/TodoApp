---
name: crud-generator
description: "Generate full CRUD implementation for a new entity across all 3 backend layers and frontend. Use when adding a new domain entity like Todo or Category."
argument-hint: "Entity name and its fields"
---

# CRUD Generator Skill

## Purpose

Generate complete CRUD (Create, Read, Update, Delete) code for a new entity across the full stack.

## Backend (implement in this order)

1. **Model** (`api/app/models/{entity}.py`) — SQLAlchemy async model with typed columns
2. **Schema** (`api/app/schemas/{entity}.py`) — Pydantic v2 schemas: `{Entity}Create`, `{Entity}Update`, `{Entity}Response`
3. **Repository** (`api/app/repositories/{entity}_repository.py`) — Async CRUD: `get_all`, `get_by_id`, `create`, `update`, `delete`
4. **Service** (`api/app/services/{entity}_service.py`) — Business logic, validation, `HTTPException` for 404/409
5. **Router** (`api/app/routes/{entity}_router.py`) — REST endpoints: GET (list), GET (by id), POST, PUT, DELETE
6. **Register** — Add router to `app/main.py` with appropriate prefix and tags
7. **Migration** — Generate Alembic revision with `alembic revision --autogenerate -m "add {entity} table"`

## Frontend (implement in this order)

1. **Types** (`web/src/types/{entity}.ts`) — TypeScript interfaces matching backend schemas
2. **Service** (`web/src/services/{entity}Service.ts`) — Axios CRUD functions
3. **Hook** (`web/src/hooks/use{Entity}s.ts`) — React Query hooks with query invalidation
4. **Components** — List component + Form component in `src/components/`
5. **Page** (`web/src/pages/{Entity}Page.tsx`) — Full page with list and create/edit form
6. **Route** — Add page route to `App.tsx`

## Conventions

- Follow all rules in `copilot-instructions.md`
- Use existing entities as reference templates when available
- All methods async on backend
- React Query invalidation after mutations on frontend
- snake_case for Python files, camelCase/PascalCase for TypeScript files
