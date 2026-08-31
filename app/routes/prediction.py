from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.service.prediction_service import predict_message
from app.schema import ComplaintCreate
from app.models import Complaint
import logging
logger = logging.getLogger(__name__)


router = APIRouter( tags=["Prediction"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/complaint")
def predict(request: ComplaintCreate, db: Session = Depends(get_db)):
    text = request.message

    result = predict_message(text)

    complaints = Complaint(
        message=request.message,
        category=result["predicted_category"],
        confidence=result["confidence"],
    )

    try:
      db.add(complaints)
      db.commit()
      db.refresh(complaints)
    except Exception as e:
            db.rollback()
            logger.error("Database error while saving message : %s", e)
            raise

    return {
        "id": complaints.id,
        **result 
    }
