import asyncio
from services.user_service import add_new_user, get_all_users
from services.meal_service import add_meal, get_meals
from services.nutrition_service import add_nutrition, get_nutrition
from services.goal_service import add_goal, get_goals
from services.leaderboard_service import add_leaderboard_entry, get_leaderboard
from services.socialsharing_service import add_social_sharing, get_social_sharing

from models.user import User
from models.meal import Meal
from models.nutrition import Nutrition
from models.goal import Goal
from models.leaderboard import Leaderboard
from models.socialsharing import SocialSharing

async def main():
    # --- Test User ---
    test_user_data = {
        "user_id": "e3b0c442-98fc-1c14-9afc-2d6a6f9c1b01",
        "username": "Alice",
        "email": "alice@example.com",
        "password_hash": "hashed_password_here"
        # created_at will be set by the service
    }
    user = User(**test_user_data)
    user_result = await add_new_user(user.model_dump())
    if isinstance(user_result, dict) and "error" in user_result:
        print("⚠️ User error:", user_result["error"])
    else:
        print("✅ User inserted with ID:", user_result)
    
    users = await get_all_users()
    print("📂 Users in database:", users)

    # --- Test Meal ---
    test_meal_data = {
        "meal_id": "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        "user_id": test_user_data["user_id"],
        "meal_name": "Chicken Salad",
        "entry_type": "scan"
        # created_at will be set by the service
    }
    meal = Meal(**test_meal_data)
    meal_result = await add_meal(meal.model_dump())
    print("✅ Meal inserted with ID:", meal_result)
    
    meals = await get_meals()
    print("📂 Meals in database:", meals)

    # --- Test Nutrition ---
    test_nutrition_data = {
        "nutrition_id": "a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d6",
        "meal_id": test_meal_data["meal_id"],
        "calories": 350,
        "protein": 30.0,
        "carbs": 20.0,
        "fats": 10.0,
        "fiber": 5.0
    }
    nutrition = Nutrition(**test_nutrition_data)
    nutrition_result = await add_nutrition(nutrition.model_dump())
    print("✅ Nutrition info inserted with ID:", nutrition_result)
    
    nutrition_list = await get_nutrition()
    print("📂 Nutrition info in database:", nutrition_list)

    # --- Test Goal ---
    test_goal_data = {
        "goal_id": "aa11bb22-cc33-dd44-ee55-ff6677889900",
        "user_id": test_user_data["user_id"],
        "daily_calories": 2000
        # created_at will be set by the service
    }
    goal = Goal(**test_goal_data)
    goal_result = await add_goal(goal.model_dump())
    print("✅ Goal inserted with ID:", goal_result)
    
    goals = await get_goals()
    print("📂 Goals in database:", goals)

    # --- Test Leaderboard ---
    test_leaderboard_data = {
        "leaderboard_id": "1111aaaa-2222-bbbb-3333-cccc4444dddd",
        "user_id": test_user_data["user_id"],
        "total_score": 1500
        # last_updated will be set by the service
    }
    leaderboard = Leaderboard(**test_leaderboard_data)
    leaderboard_result = await add_leaderboard_entry(leaderboard.model_dump())
    print("✅ Leaderboard entry inserted with ID:", leaderboard_result)
    
    leaderboard_list = await get_leaderboard()
    print("📂 Leaderboard in database:", leaderboard_list)

    # --- Test Social Sharing ---
    test_socialsharing_data = {
        "share_id": "aaaabbbb-cccc-dddd-eeee-ffff11112222",
        "user_id": test_user_data["user_id"],
        "meal_id": test_meal_data["meal_id"],
        "share_platform": "Facebook"
        # shared_at will be set by the service
    }
    socialsharing = SocialSharing(**test_socialsharing_data)
    socialsharing_result = await add_social_sharing(socialsharing.model_dump())
    print("✅ Social sharing record inserted with ID:", socialsharing_result)
    
    socialsharing_list = await get_social_sharing()
    print("📂 Social sharing records in database:", socialsharing_list)

if __name__ == "__main__":
    asyncio.run(main())
