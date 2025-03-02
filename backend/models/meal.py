from pydantic import BaseModel
from datetime import datetime

class Meal(BaseModel):
    meal_id: str
    user_id: str
    meal_name: str
    entry_type: str  # "manual" or "scan"
    created_at: datetime = None

    class Config:
        schema_extra = {
            "example": {
                "meal_id": "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
                "user_id": "e3b0c442-98fc-1c14-9afc-2d6a6f9c1b01",
                "meal_name": "Chicken Salad",
                "entry_type": "scan",
                "created_at": "2025-03-01T12:00:00"
            }
        }
