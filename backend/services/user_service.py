from config.db import db
from datetime import datetime

# Create a new user
async def add_new_user(user_data: dict):
    # Set the createdAt field if not provided
    if "createdAt" not in user_data or user_data["createdAt"] is None:
        user_data["createdAt"] = datetime.utcnow()

    # Check if a user with the same email already exists
    existing_user = await db["users"].find_one({"email": user_data["email"]})
    if existing_user:
        return {"error": "User already exists"}

    result = await db["users"].insert_one(user_data)
    return {"message": "User registered successfully", "user_id": str(result.inserted_id)}

# Retrieve all users
async def get_all_users(limit: int = 10):
    users = await db["users"].find({}, {"_id": 0}).to_list(limit)
    return users

# Retrieve a user by email
async def get_user_by_email(email: str):
    return await db["users"].find_one({"email": email}, {"_id": 0})

# Update a user (by email for example)
async def update_user(email: str, update_data: dict):
    updated = await db["users"].find_one_and_update(
        {"email": email},
        {"$set": update_data},
        return_document=True
    )
    return updated

# Delete a user (by email)
async def delete_user(email: str):
    result = await db["users"].delete_one({"email": email})
    if result.deleted_count == 1:
        return {"message": "User deleted successfully"}
    return {"error": "User not found"}
