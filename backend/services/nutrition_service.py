from config.db import db

async def add_nutrition(nutrition_data: dict):
    result = await db["nutrition"].insert_one(nutrition_data)
    return result.inserted_id

async def get_nutrition(limit: int = 10):
    nutrition_list = await db["nutrition"].find({}).to_list(limit)
    return nutrition_list
