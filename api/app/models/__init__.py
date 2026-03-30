"""SQLAlchemy ORM model definitions."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all ORM models."""

    pass


from app.models.todo import Todo  # noqa: E402, F401
