from sqlalchemy import Column, Float, Integer, String, DateTime
from datetime import datetime

from app.database import Base

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String(600), nullable=False)
    category = Column(String(50), nullable=False)
    confidence = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)