from pydantic import BaseModel
from datetime import datetime

class Leaderboard(BaseModel):
    leaderboard_id: str
    user_id: str
    total_score: int
    last_updated: datetime = None

    class Config:
        json_schema_extra = {
            "example": {
                "leaderboard_id": "1111aaaa-2222-bbbb-3333-cccc4444dddd",
                "user_id": "e3b0c442-98fc-1c14-9afc-2d6a6f9c1b01",
                "total_score": 1500,
                "last_updated": "2025-03-04T10:00:00"
            }
        }
