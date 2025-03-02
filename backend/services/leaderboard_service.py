from config.db import db
from datetime import datetime

async def add_leaderboard_entry(entry_data: dict):
    if "last_updated" not in entry_data or entry_data["last_updated"] is None:
        entry_data["last_updated"] = datetime.utcnow()
    result = await db["leaderboard"].insert_one(entry_data)
    return result.inserted_id

async def get_leaderboard(limit: int = 10):
    leaderboard = await db["leaderboard"].find({}).to_list(limit)
    return leaderboard
