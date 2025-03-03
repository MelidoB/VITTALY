from pydantic import BaseModel
from datetime import datetime

class Goal(BaseModel):
    goal_id: str
    user_id: str
    daily_calories: int
    created_at: datetime = None

    class Config:
        json_schema_extra = {
            "example": {
                "goal_id": "aa11bb22-cc33-dd44-ee55-ff6677889900",
                "user_id": "e3b0c442-98fc-1c14-9afc-2d6a6f9c1b01",
                "daily_calories": 2000,
                "created_at": "2025-03-01T00:00:00"
            }
        }
