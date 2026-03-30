"""FastAPI application factory and configuration."""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.todo_router import router as todo_router

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """Create and configure the FastAPI application.

    Returns:
        FastAPI: The configured application instance.
    """
    application = FastAPI(
        title="TodoApp API",
        description="A full-stack Todo application API",
        version="0.1.0",
    )

    # CORS configuration — allow the Vite dev server
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @application.get("/", tags=["health"])
    async def health_check() -> dict[str, str]:
        """Return a simple health check response."""
        return {"status": "ok"}

    # Register routers
    application.include_router(todo_router)

    logger.info("TodoApp API initialized")
    return application


app = create_app()
