"""Todo service — business logic for Todo operations."""

import logging

from fastapi import HTTPException, status

from app.models.todo import Todo
from app.repositories.todo_repository import TodoRepository
from app.schemas.todo import TodoCreate, TodoUpdate

logger = logging.getLogger(__name__)


class TodoService:
    """Encapsulates all business rules for Todo operations."""

    def __init__(self, repo: TodoRepository) -> None:
        """Initialize with a TodoRepository instance.

        Args:
            repo: The data-access repository for todos.
        """
        self.repo = repo

    async def get_all(self) -> list[Todo]:
        """Return all todos.

        Returns:
            A list of Todo objects.
        """
        return await self.repo.get_all()

    async def get_by_id(self, todo_id: int) -> Todo:
        """Return a single todo by ID, or raise 404.

        Args:
            todo_id: The primary key of the todo.

        Returns:
            The Todo object.

        Raises:
            HTTPException: 404 if the todo is not found.
        """
        todo = await self.repo.get_by_id(todo_id)
        if todo is None:
            logger.warning("Todo id=%s not found", todo_id)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Todo with id {todo_id} not found",
            )
        return todo

    async def create(self, data: TodoCreate) -> Todo:
        """Create a new todo from validated input.

        Args:
            data: The validated creation payload.

        Returns:
            The newly created Todo.
        """
        todo = Todo(title=data.title, description=data.description)
        return await self.repo.create(todo)

    async def update(self, todo_id: int, data: TodoUpdate) -> Todo:
        """Update an existing todo with partial data.

        Args:
            todo_id: The primary key of the todo to update.
            data: The validated update payload (partial).

        Returns:
            The updated Todo.

        Raises:
            HTTPException: 404 if the todo is not found.
        """
        todo = await self.get_by_id(todo_id)
        update_fields = data.model_dump(exclude_unset=True)
        for field, value in update_fields.items():
            setattr(todo, field, value)
        return await self.repo.update(todo)

    async def delete(self, todo_id: int) -> None:
        """Delete a todo by ID.

        Args:
            todo_id: The primary key of the todo to delete.

        Raises:
            HTTPException: 404 if the todo is not found.
        """
        todo = await self.get_by_id(todo_id)
        await self.repo.delete(todo)
