from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schema import  ComplaintResponse
from app.database import SessionLocal
from app.models import Complaint
import logging
logger = logging.getLogger(__name__)

router = APIRouter( tags=["History"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/complaints",response_model=list[ComplaintResponse])
def get_history(
    category: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Complaint)

    if category is not None:
        query = query.filter(Complaint.category == category)

    return query.all()

@router.get("/complaints/{complaints_id}",response_model=ComplaintResponse)
def get_classification(complaints_id: int, db: Session = Depends(get_db)):
    complaints = db.query(Complaint).filter(Complaint.id == complaints_id).first()

    if complaints is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return complaints