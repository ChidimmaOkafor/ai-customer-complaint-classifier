from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class ComplaintCreate(BaseModel):
        message: str = Field(..., example="I am not satisfied with the product I received.", min_length=1, max_length=600)

class ComplaintResponse(BaseModel):
        id: int
        message:str
        category: str
        confidence : float
        created_at: datetime


    
model_config = ConfigDict(from_attributes = True)