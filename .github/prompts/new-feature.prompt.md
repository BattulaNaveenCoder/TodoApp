---
description: "Generate a feature implementation using the RTACCO pattern"
agent: "agent"
argument-hint: "Describe the feature to implement"
---

You are implementing a new feature for the TodoApp. Follow the RTACCO pattern:

**Role**: Senior full-stack developer
**Task**: Implement the feature described below
**Audience**: Enterprise production codebase
**Context**: Monorepo — `/api` (FastAPI 3-layer) and `/web` (React + TS + React Query)
**Constraints**: Follow all rules in `copilot-instructions.md`. All affected layers must be implemented.
**Output**: Working code for all affected layers

## Backend (implement in this order)

1. **Model** (`app/models/`) — SQLAlchemy ORM table definition
2. **Schema** (`app/schemas/`) — Pydantic v2 Create, Update, Response DTOs
3. **Repository** (`app/repositories/`) — Async CRUD data access
4. **Service** (`app/services/`) — Business logic and validation
5. **Router** (`app/routes/`) — FastAPI endpoints
6. **Register** — Add router to `app/main.py`
7. **Migration** — Generate Alembic migration if model changed

## Frontend (implement in this order)

1. **Types** (`src/types/`) — TypeScript interfaces matching backend schemas
2. **Service** (`src/services/`) — Axios API client functions
3. **Hook** (`src/hooks/`) — React Query hooks per domain
4. **Component** (`src/components/`) — Reusable UI pieces
5. **Page** (`src/pages/`) — Full page composition
6. **Route** — Register in `App.tsx`
