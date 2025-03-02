from config.db import db
from datetime import datetime

async def add_social_sharing(share_data: dict):
    if "shared_at" not in share_data or share_data["shared_at"] is None:
        share_data["shared_at"] = datetime.utcnow()
    result = await db["socialsharing"].insert_one(share_data)
    return result.inserted_id

async def get_social_sharing(limit: int = 10):
    shares = await db["socialsharing"].find({}).to_list(limit)
    return shares
