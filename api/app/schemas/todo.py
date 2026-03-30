"""Pydantic v2 schemas for Todo request/response DTOs."""

import datetime

from pydantic import BaseModel, ConfigDict, Field


class TodoCreate(BaseModel):
    """Schema for creating a new todo."""

    title: str = Field(..., min_length=1, max_length=200, description="Todo title")
    description: str | None = Field(None, description="Optional detailed description")


class TodoUpdate(BaseModel):
    """Schema for updating an existing todo. All fields optional."""

    title: str | None = Field(None, min_length=1, max_length=200, description="Todo title")
    description: str | None = Field(None, description="Optional detailed description")
    is_completed: bool | None = Field(None, description="Completion status")


class TodoResponse(BaseModel):
    """Schema for returning a todo to the client."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    is_completed: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
