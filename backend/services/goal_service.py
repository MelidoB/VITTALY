from config.db import db
from datetime import datetime

async def add_goal(goal_data: dict):
    if "created_at" not in goal_data or goal_data["created_at"] is None:
        goal_data["created_at"] = datetime.utcnow()
    result = await db["goals"].insert_one(goal_data)
    return result.inserted_id

async def get_goals(limit: int = 10):
    goals = await db["goals"].find({}).to_list(limit)
    return goals

async def get_goal_by_id(goal_id: str):
    return await db["goals"].find_one({"goal_id": goal_id}, {"_id": 0})

async def update_goal(goal_id: str, update_data: dict):
    updated = await db["goals"].find_one_and_update(
        {"goal_id": goal_id},
        {"$set": update_data},
        return_document=True
    )
    return updated

async def delete_goal(goal_id: str):
    result = await db["goals"].delete_one({"goal_id": goal_id})
    if result.deleted_count == 1:
        return {"message": "Goal deleted successfully"}
    return {"error": "Goal not found"}
