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
