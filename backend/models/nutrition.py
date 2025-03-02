from pydantic import BaseModel
from typing import Optional

class Nutrition(BaseModel):
    nutrition_id: str
    meal_id: str
    calories: int
    protein: Optional[float] = None
    carbs: Optional[float] = None
    fats: Optional[float] = None
    fiber: Optional[float] = None

    class Config:
        schema_extra = {
            "example": {
                "nutrition_id": "a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d6",
                "meal_id": "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
                "calories": 350,
                "protein": 30.0,
                "carbs": 20.0,
                "fats": 10.0,
                "fiber": 5.0
            }
        }
