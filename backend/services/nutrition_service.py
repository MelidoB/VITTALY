from config.db import db

async def add_nutrition(nutrition_data: dict):
    result = await db["nutrition"].insert_one(nutrition_data)
    return result.inserted_id

async def get_nutrition(limit: int = 10):
    nutrition_list = await db["nutrition"].find({}).to_list(limit)
    return nutrition_list

async def get_nutrition_by_id(nutrition_id: str):
    return await db["nutrition"].find_one({"nutrition_id": nutrition_id}, {"_id": 0})

async def update_nutrition(nutrition_id: str, update_data: dict):
    updated = await db["nutrition"].find_one_and_update(
        {"nutrition_id": nutrition_id},
        {"$set": update_data},
        return_document=True
    )
    return updated

async def delete_nutrition(nutrition_id: str):
    result = await db["nutrition"].delete_one({"nutrition_id": nutrition_id})
    if result.deleted_count == 1:
        return {"message": "Nutrition record deleted successfully"}
    return {"error": "Nutrition record not found"}
