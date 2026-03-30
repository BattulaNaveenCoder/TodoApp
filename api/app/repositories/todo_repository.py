"""Todo repository — all database queries for the Todo model."""

import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.todo import Todo

logger = logging.getLogger(__name__)


class TodoRepository:
    """Handles all data-access operations for Todo entities."""

    def __init__(self, db: AsyncSession) -> None:
        """Initialize with an async database session.

        Args:
            db: The SQLAlchemy async session.
        """
        self.db = db

    async def get_all(self) -> list[Todo]:
        """Return all todos ordered by creation date descending.

        Returns:
            A list of Todo ORM objects.
        """
        result = await self.db.execute(
            select(Todo).order_by(Todo.created_at.desc())
        )
        return list(result.scalars().all())

    async def get_by_id(self, todo_id: int) -> Todo | None:
        """Return a single todo by its ID, or None if not found.

        Args:
            todo_id: The primary key of the todo.

        Returns:
            The Todo object or None.
        """
        return await self.db.get(Todo, todo_id)

    async def create(self, todo: Todo) -> Todo:
        """Insert a new todo into the database.

        Args:
            todo: The Todo ORM object to persist.

        Returns:
            The persisted Todo with generated fields populated.
        """
        self.db.add(todo)
        await self.db.flush()
        await self.db.refresh(todo)
        logger.info("Created todo id=%s title=%r", todo.id, todo.title)
        return todo

    async def update(self, todo: Todo) -> Todo:
        """Persist changes to an existing todo.

        Args:
            todo: The modified Todo ORM object.

        Returns:
            The updated Todo.
        """
        await self.db.flush()
        await self.db.refresh(todo)
        logger.info("Updated todo id=%s", todo.id)
        return todo

    async def delete(self, todo: Todo) -> None:
        """Remove a todo from the database.

        Args:
            todo: The Todo ORM object to delete.
        """
        await self.db.delete(todo)
        await self.db.flush()
        logger.info("Deleted todo id=%s", todo.id)
