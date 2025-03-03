from fastapi import APIRouter, HTTPException
from models.goal import Goal
from services.goal_service import (
    add_goal,
    get_goals,
    get_goal_by_id,
    update_goal,
    delete_goal
)

router = APIRouter()

@router.post("/", response_model=dict)
async def create_goal(goal: Goal):
    result = await add_goal(goal.model_dump())
    return {"goal_id": result}

@router.get("/", response_model=list[Goal])
async def list_goals():
    return await get_goals()

@router.get("/{goal_id}", response_model=Goal)
async def read_goal(goal_id: str):
    goal = await get_goal_by_id(goal_id)
    if goal is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal

@router.put("/{goal_id}", response_model=Goal)
async def update_goal_endpoint(goal_id: str, goal: Goal):
    updated = await update_goal(goal_id, goal.model_dump())
    if updated is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    return updated

@router.delete("/{goal_id}", response_model=dict)
async def delete_goal_endpoint(goal_id: str):
    result = await delete_goal(goal_id)
    if not result:
        raise HTTPException(status_code=404, detail="Goal not found")
    return {"detail": "Goal deleted successfully"}
