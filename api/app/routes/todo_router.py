"""Todo router — HTTP endpoints for Todo CRUD operations."""

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.repositories.todo_repository import TodoRepository
from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdate
from app.services.todo_service import TodoService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/todos", tags=["todos"])


def get_todo_service(db: AsyncSession = Depends(get_db)) -> TodoService:
    """Dependency injector: build the TodoService with its repository.

    Args:
        db: The async database session from get_db().

    Returns:
        A fully wired TodoService instance.
    """
    repo = TodoRepository(db)
    return TodoService(repo)


TodoServiceDep = Annotated[TodoService, Depends(get_todo_service)]


@router.get("/", response_model=list[TodoResponse])
async def get_todos(service: TodoServiceDep) -> list[TodoResponse]:
    """Get all todos.

    Returns:
        A list of all todo items.
    """
    todos = await service.get_all()
    return [TodoResponse.model_validate(t) for t in todos]


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: int, service: TodoServiceDep) -> TodoResponse:
    """Get a single todo by ID.

    Args:
        todo_id: The primary key of the todo.
        service: The injected TodoService.

    Returns:
        The requested todo item.
    """
    todo = await service.get_by_id(todo_id)
    return TodoResponse.model_validate(todo)


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(data: TodoCreate, service: TodoServiceDep) -> TodoResponse:
    """Create a new todo.

    Args:
        data: The creation payload.
        service: The injected TodoService.

    Returns:
        The newly created todo item.
    """
    todo = await service.create(data)
    return TodoResponse.model_validate(todo)


@router.patch("/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: int, data: TodoUpdate, service: TodoServiceDep
) -> TodoResponse:
    """Update an existing todo (partial update).

    Args:
        todo_id: The primary key of the todo to update.
        data: The update payload (partial).
        service: The injected TodoService.

    Returns:
        The updated todo item.
    """
    todo = await service.update(todo_id, data)
    return TodoResponse.model_validate(todo)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, service: TodoServiceDep) -> None:
    """Delete a todo by ID.

    Args:
        todo_id: The primary key of the todo to delete.
        service: The injected TodoService.
    """
    await service.delete(todo_id)
