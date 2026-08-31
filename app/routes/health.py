from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.service.prediction_service import (
    category_model,
)

router = APIRouter(prefix="/health", tags=["Health"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        database_status = "connected"
    except Exception:
        database_status = "disconnected"

    return {
        "status": "healthy",
        "database": database_status,
        "category_model": {
            "status": "loaded",
            "version": "v2"
        } if category_model else {"status": "not loaded"},
    }