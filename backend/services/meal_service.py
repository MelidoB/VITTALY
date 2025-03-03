from config.db import db
from datetime import datetime

async def add_meal(meal_data: dict):
    if "created_at" not in meal_data or meal_data["created_at"] is None:
        meal_data["created_at"] = datetime.utcnow()
    result = await db["meals"].insert_one(meal_data)
    return result.inserted_id

async def get_meals(limit: int = 10):
    meals = await db["meals"].find({}).to_list(limit)
    return meals

async def get_meal_by_id(meal_id: str):
    return await db["meals"].find_one({"meal_id": meal_id}, {"_id": 0})

async def update_meal(meal_id: str, update_data: dict):
    updated = await db["meals"].find_one_and_update(
        {"meal_id": meal_id},
        {"$set": update_data},
        return_document=True
    )
    return updated

async def delete_meal(meal_id: str):
    result = await db["meals"].delete_one({"meal_id": meal_id})
    if result.deleted_count == 1:
        return {"message": "Meal deleted successfully"}
    return {"error": "Meal not found"}
