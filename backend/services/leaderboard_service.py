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

async def get_leaderboard_by_id(leaderboard_id: str):
    return await db["leaderboard"].find_one({"leaderboard_id": leaderboard_id}, {"_id": 0})

async def update_leaderboard(leaderboard_id: str, update_data: dict):
    updated = await db["leaderboard"].find_one_and_update(
        {"leaderboard_id": leaderboard_id},
        {"$set": update_data},
        return_document=True
    )
    return updated

async def delete_leaderboard(leaderboard_id: str):
    result = await db["leaderboard"].delete_one({"leaderboard_id": leaderboard_id})
    if result.deleted_count == 1:
        return {"message": "Leaderboard entry deleted successfully"}
    return {"error": "Leaderboard entry not found"}
