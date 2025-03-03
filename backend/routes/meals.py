from fastapi import APIRouter, HTTPException
from models.meal import Meal
from services.meal_service import (
    add_meal,
    get_meals,
    get_meal_by_id,
    update_meal,
    delete_meal
)

router = APIRouter()

@router.post("/", response_model=dict)
async def create_meal(meal: Meal):
    result = await add_meal(meal.model_dump())
    return {"meal_id": result}

@router.get("/", response_model=list[Meal])
async def list_meals():
    return await get_meals()

@router.get("/{meal_id}", response_model=Meal)
async def read_meal(meal_id: str):
    meal = await get_meal_by_id(meal_id)
    if meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return meal

@router.put("/{meal_id}", response_model=Meal)
async def update_meal_endpoint(meal_id: str, meal: Meal):
    updated = await update_meal(meal_id, meal.model_dump())
    if updated is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return updated

@router.delete("/{meal_id}", response_model=dict)
async def delete_meal_endpoint(meal_id: str):
    result = await delete_meal(meal_id)
    if not result:
        raise HTTPException(status_code=404, detail="Meal not found")
    return {"detail": "Meal deleted successfully"}
