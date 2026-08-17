from fastapi import FastAPI
import logging 

from app.core.config import settings
from app.core.logging import configure_logging
from app.routers.health import router as health_router
from app.routers.meetings import router as meetings_router


configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title = settings.app_name,
    description = "Meeting knowledge assistant built with Google Cloud and Gemini.",
    version = settings.app_version
)

@app.on_event("startup")
def startup_event() -> None:
    logger.info(
        "Application started: name=%s version=%s environment=%s",
        settings.app_name,
        settings.app_version,
        settings.environment
    )

#Registers the routers with the main application, making FastAPI aware of it.
app.include_router(health_router)
app.include_router(meetings_router)


@app.get("/")
def root() -> dict[str, str]:
    logger.info("Root endpoint called")
    
    return {
        "application":settings.app_name,
        "version" : settings.app_version,
        "environment": settings.environment
    }




