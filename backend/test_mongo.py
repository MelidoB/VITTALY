import asyncio
from services.user_service import add_new_user, get_all_users
from models.user import User

async def main():
    # Create a test user using the Pydantic model
    test_user_data = {
        "username": "Alice",
        "email": "alice@example.com",
        "passwordHash": "hashed_password_here"
    }
    user = User(**test_user_data)
    
    # Add the user using the controller
    result = await add_new_user(user.dict())
    if "error" in result:
        print("⚠️", result["error"])
    else:
        print("✅", result)
    
    # Retrieve all users and display them
    users = await get_all_users()
    print("📂 Users in database:", users)

if __name__ == "__main__":
    asyncio.run(main())
