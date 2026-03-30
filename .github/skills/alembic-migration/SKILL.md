---
name: alembic-migration
description: "Generate and run Alembic database migrations for the async SQLAlchemy + SQL Server stack. Use when adding new tables, altering columns, adding foreign keys, or making any schema change. Handles the aioodbc async driver and SQL Server dialect specifics."
argument-hint: "[migration description]"
---

# Alembic Migration Skill

Generate and manage async Alembic migrations for the SQL Server database.

## Environment

- **Engine**: SQLAlchemy 2.x async with `create_async_engine`
- **Driver**: `aioodbc` (connection string: `mssql+aioodbc://...`)
- **Config**: `api/alembic.ini` (no sqlalchemy.url — loaded from `app/db/session.py`)
- **Env file**: `api/alembic/env.py` (async migrations via `asyncio.run`)
- **Models**: `api/app/models/__init__.py` imports all models; `Base.metadata` is used by Alembic

## Before Generating

1. Ensure the new model is imported in `api/app/models/__init__.py`
2. Ensure the `.env` file has a valid `DATABASE_URL`

## Generate a Migration (autogenerate)

```bash
cd api
python -m alembic revision --autogenerate -m "describe_change_here"
```

If autogenerate fails (e.g., no DB connection), create the migration file manually:

```
api/alembic/versions/NNNN_describe_change_here.py
```

Use sequential revision IDs: `0001`, `0002`, etc. Set `down_revision` to the previous migration ID.

## Run Migrations

```bash
cd api
python -m alembic upgrade head      # Apply all pending
python -m alembic downgrade -1      # Rollback last one
python -m alembic current           # Show current revision
python -m alembic history           # Show migration history
```

## Migration File Template

```python
"""describe change here

Revision ID: NNNN
Revises: previous_id_or_None
Create Date: YYYY-MM-DD
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "NNNN"
down_revision: Union[str, None] = "previous_id"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Apply schema change."""
    pass


def downgrade() -> None:
    """Revert schema change."""
    pass
```

## SQL Server Specifics

- Use `sa.String(length=N)` instead of unbounded `sa.String()` for indexed columns
- Use `sa.DateTime(timezone=True)` for timestamp columns
- Use `server_default=sa.func.now()` for auto-timestamps
- Boolean columns: use `server_default=sa.text("0")` for False
- Foreign keys: always name constraints explicitly for clean downgrades
