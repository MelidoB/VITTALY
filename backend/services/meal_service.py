from config.db import db
from datetime import datetime

async def add_meal(meal_data: dict):
    # Ensure created_at is set
    if "created_at" not in meal_data or meal_data["created_at"] is None:
        meal_data["created_at"] = datetime.utcnow()
    result = await db["meals"].insert_one(meal_data)
    return result.inserted_id

async def get_meals(limit: int = 10):
    meals = await db["meals"].find({}).to_list(limit)
    return meals
