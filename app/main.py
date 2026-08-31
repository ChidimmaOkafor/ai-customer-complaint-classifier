from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import logging

from app.routes.health import router as health_router
from app.routes.prediction import router as prediction_router
from app.routes.history import router as history_router


logger = logging.getLogger(__name__)

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(
        "Invalid request received: %s",
        exc.errors()
    )

    return JSONResponse(
        status_code=422,
        content={
            "detail": exc.errors()
        }
    )

app.include_router(health_router)
app.include_router(prediction_router)
app.include_router(history_router)
