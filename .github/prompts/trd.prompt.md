---
description: "Technical Requirements Document for the TodoApp — defines architecture, data model, API contracts, and tech stack decisions"
---

# TodoApp — Technical Requirements Document (TRD)

## 1. System Architecture

```
┌──────────────┐       ┌──────────────────────────────────────────┐       ┌────────────┐
│   Browser    │──────▸│           FastAPI Backend                │──────▸│ SQL Server │
│  React + TS  │  HTTP │  Routes → Services → Repositories       │  SQL  │  Express   │
│  port 5173   │◂──────│  port 8000                               │◂──────│  port 1433 │
└──────────────┘       └──────────────────────────────────────────┘       └────────────┘
       │
       └── Vite dev proxy: /api/* → http://localhost:8000/*
```

### 1.1 Backend — 3-Layer Architecture

| Layer | Location | Responsibility | Rules |
|-------|----------|---------------|-------|
| **Presentation** | `app/routes/` | HTTP endpoints, Pydantic validation, response serialization | No business logic, no DB access |
| **Business Logic** | `app/services/` | Rules, orchestration, `HTTPException` for violations | No SQLAlchemy queries, no HTTP knowledge beyond exceptions |
| **Data Access** | `app/repositories/` | SQLAlchemy queries, ORM operations | No business logic, no HTTP knowledge |

### 1.2 Dependency Injection Flow

```python
get_db() → Repository(db) → Service(repo) → Route(service)
```

Session lifecycle: created per request, committed on success, rolled back on exception, always closed.

### 1.3 Frontend Layers

| Layer | Location | Responsibility |
|-------|----------|---------------|
| Pages | `src/pages/` | Route-level components |
| Components | `src/components/` | Reusable UI pieces |
| Hooks | `src/hooks/` | React Query hooks per domain |
| Services | `src/services/` | Axios API client functions |
| Types | `src/types/` | TypeScript interfaces matching backend DTOs |

## 2. Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| Runtime | Python | 3.12+ |
| API Framework | FastAPI | >= 0.115 |
| ASGI Server | Uvicorn | >= 0.30 |
| ORM | SQLAlchemy (async) | >= 2.0 |
| Migrations | Alembic | >= 1.13 |
| DB Driver | aioodbc | >= 0.5 |
| Validation | Pydantic v2 | >= 2.0 |
| Frontend Runtime | Node.js | 20+ |
| UI Library | React | 19 |
| Build Tool | Vite | 8 |
| Server State | TanStack React Query | 5 |
| HTTP Client | Axios | 1.x |
| Language | TypeScript | 5.9 |
| Database | SQL Server Express | 2019+ |

## 3. Data Model

### 3.1 `todos` Table (Phase 1)

| Column | Type | Constraints |
|--------|------|------------|
| `id` | `INT` | PK, auto-increment |
| `title` | `NVARCHAR(200)` | NOT NULL |
| `description` | `NTEXT` | NULLABLE |
| `is_completed` | `BIT` | NOT NULL, DEFAULT 0 |
| `created_at` | `DATETIMEOFFSET` | NOT NULL, DEFAULT GETDATE() |
| `updated_at` | `DATETIMEOFFSET` | NOT NULL, DEFAULT GETDATE() |

### 3.2 `categories` Table (Phase 3)

| Column | Type | Constraints |
|--------|------|------------|
| `id` | `INT` | PK, auto-increment |
| `name` | `NVARCHAR(100)` | NOT NULL, UNIQUE |
| `created_at` | `DATETIMEOFFSET` | NOT NULL, DEFAULT GETDATE() |

### 3.3 Relationship (Phase 3)

- `todos.category_id` → `categories.id` (FK, NULLABLE, ON DELETE SET NULL)

## 4. API Contract

### 4.1 Todo Endpoints

| Method | Endpoint | Request Body | Response | Status |
|--------|----------|-------------|----------|--------|
| `GET` | `/todos/` | — | `TodoResponse[]` | 200 |
| `GET` | `/todos/{id}` | — | `TodoResponse` | 200 / 404 |
| `POST` | `/todos/` | `TodoCreate` | `TodoResponse` | 201 |
| `PATCH` | `/todos/{id}` | `TodoUpdate` | `TodoResponse` | 200 / 404 |
| `DELETE` | `/todos/{id}` | — | — | 204 / 404 |

### 4.2 Category Endpoints (Phase 3)

| Method | Endpoint | Request Body | Response | Status |
|--------|----------|-------------|----------|--------|
| `GET` | `/categories/` | — | `CategoryResponse[]` | 200 |
| `GET` | `/categories/{id}` | — | `CategoryResponse` | 200 / 404 |
| `POST` | `/categories/` | `CategoryCreate` | `CategoryResponse` | 201 / 409 |
| `PATCH` | `/categories/{id}` | `CategoryUpdate` | `CategoryResponse` | 200 / 404 / 409 |
| `DELETE` | `/categories/{id}` | — | — | 204 / 404 |

## 5. Pydantic Schemas

### TodoCreate
```json
{ "title": "string (1-200)", "description": "string | null" }
```

### TodoUpdate
```json
{ "title?": "string (1-200)", "description?": "string | null", "is_completed?": "boolean" }
```

### TodoResponse
```json
{ "id": "int", "title": "string", "description": "string | null", "is_completed": "boolean", "created_at": "datetime", "updated_at": "datetime" }
```

### CategoryCreate (Phase 3)
```json
{ "name": "string (1-100)" }
```

### CategoryResponse (Phase 3)
```json
{ "id": "int", "name": "string", "created_at": "datetime" }
```

## 6. Error Handling Strategy

| Status | Meaning | When |
|--------|---------|------|
| 200 | OK | Successful GET / PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Malformed request body |
| 404 | Not Found | Entity ID does not exist |
| 409 | Conflict | Unique constraint violation (e.g., duplicate category name) |
| 422 | Unprocessable Entity | Pydantic validation failure (automatic) |
| 500 | Internal Server Error | Unhandled exception (never expose details to client) |

## 7. Security Considerations

- No hardcoded secrets — use `.env` files (gitignored)
- All user input validated via Pydantic at the route level
- Parameterized SQLAlchemy queries — no raw SQL string interpolation
- CORS restricted to `http://localhost:5173` (Vite dev server)
- No sensitive data in API error responses

## 8. Database Connection

```
mssql+aioodbc:///?odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=TodoDb;Trusted_Connection=yes;
```

Default is hardcoded in `app/db/session.py`. Can be overridden via `api/.env` as `DATABASE_URL`. Loaded via `pydantic-settings`.
