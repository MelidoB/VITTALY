from fastapi import APIRouter, HTTPException
from models.nutrition import Nutrition
from services.nutrition_service import (
    add_nutrition,
    get_nutrition,
    get_nutrition_by_id,
    update_nutrition,
    delete_nutrition
)

router = APIRouter()

@router.post("/", response_model=dict)
async def create_nutrition(nutrition: Nutrition):
    result = await add_nutrition(nutrition.model_dump())
    return {"nutrition_id": result}

@router.get("/", response_model=list[Nutrition])
async def list_nutrition():
    return await get_nutrition()

@router.get("/{nutrition_id}", response_model=Nutrition)
async def read_nutrition(nutrition_id: str):
    record = await get_nutrition_by_id(nutrition_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Nutrition record not found")
    return record

@router.put("/{nutrition_id}", response_model=Nutrition)
async def update_nutrition_endpoint(nutrition_id: str, nutrition: Nutrition):
    updated = await update_nutrition(nutrition_id, nutrition.model_dump())
    if updated is None:
        raise HTTPException(status_code=404, detail="Nutrition record not found")
    return updated

@router.delete("/{nutrition_id}", response_model=dict)
async def delete_nutrition_endpoint(nutrition_id: str):
    result = await delete_nutrition(nutrition_id)
    if not result:
        raise HTTPException(status_code=404, detail="Nutrition record not found")
    return {"detail": "Nutrition record deleted successfully"}
