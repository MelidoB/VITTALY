from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class User(BaseModel):
    user_id: str
    username: str
    email: EmailStr
    password_hash: str
    created_at: Optional[datetime] = None  # Allow None if not provided

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "e3b0c442-98fc-1c14-9afc-2d6a6f9c1b01",
                "username": "Alice",
                "email": "alice@example.com",
                "password_hash": "hashed_password_here",
                "created_at": "2025-03-01T08:30:00"
            }
        }
