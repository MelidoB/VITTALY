import os
import requests

# Load USDA API Key GitHub Secrets
USDA_API_KEY = os.getenv("USDA_API_KEY")
USDA_API_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

if not USDA_API_KEY:
    raise ValueError("Missing USDA API Key! Set it in environment variables.")

def get_nutrition_from_usda(food_name):
    params = {
        "query": food_name,
        "api_key": USDA_API_KEY,
    }
    response = requests.get(USDA_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if "foods" in data and len(data["foods"]) > 0:
            food_info = data["foods"][0]
            nutrients = {nutrient["nutrientName"]: nutrient["value"] for nutrient in food_info["foodNutrients"]}
            
            return {
                "calories": nutrients.get("Energy", "Unknown"),
                "protein": nutrients.get("Protein", "Unknown"),
                "carbs": nutrients.get("Carbohydrate, by difference", "Unknown"),
                "fats": nutrients.get("Total lipid (fat)", "Unknown"),
                "fiber": nutrients.get("Fiber, total dietary", "Unknown"), 
            }
    return {"calories": "Unknown", "protein": "Unknown", "carbs": "Unknown", "fats": "Unknown", "fiber": "Unknown"}
