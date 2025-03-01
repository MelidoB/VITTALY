from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    username: str
    email: EmailStr
    passwordHash: str  # Remember: In production, use proper password hashing
    createdAt: datetime = None  # This can be set when inserting the document

    class Config:
        schema_extra = {
            "example": {
                "username": "Alice",
                "email": "alice@example.com",
                "passwordHash": "hashed_password_here"
            }
        }
