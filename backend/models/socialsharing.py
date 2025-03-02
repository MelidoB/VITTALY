from pydantic import BaseModel
from datetime import datetime

class SocialSharing(BaseModel):
    share_id: str
    user_id: str
    meal_id: str
    share_platform: str
    shared_at: datetime = None

    class Config:
        schema_extra = {
            "example": {
                "share_id": "aaaabbbb-cccc-dddd-eeee-ffff11112222",
                "user_id": "e3b0c442-98fc-1c14-9afc-2d6a6f9c1b01",
                "meal_id": "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
                "share_platform": "Facebook",
                "shared_at": "2025-03-01T14:00:00"
            }
        }
