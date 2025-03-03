from fastapi import APIRouter, HTTPException
from models.leaderboard import Leaderboard
from services.leaderboard_service import (
    add_leaderboard_entry,
    get_leaderboard,
    get_leaderboard_by_id,
    update_leaderboard,
    delete_leaderboard
)

router = APIRouter()

@router.post("/", response_model=dict)
async def create_leaderboard_entry(entry: Leaderboard):
    result = await add_leaderboard_entry(entry.model_dump())
    return {"leaderboard_id": result}

@router.get("/", response_model=list[Leaderboard])
async def list_leaderboard():
    return await get_leaderboard()

@router.get("/{leaderboard_id}", response_model=Leaderboard)
async def read_leaderboard(leaderboard_id: str):
    entry = await get_leaderboard_by_id(leaderboard_id)
    if entry is None:
        raise HTTPException(status_code=404, detail="Leaderboard entry not found")
    return entry

@router.put("/{leaderboard_id}", response_model=Leaderboard)
async def update_leaderboard_endpoint(leaderboard_id: str, entry: Leaderboard):
    updated = await update_leaderboard(leaderboard_id, entry.model_dump())
    if updated is None:
        raise HTTPException(status_code=404, detail="Leaderboard entry not found")
    return updated

@router.delete("/{leaderboard_id}", response_model=dict)
async def delete_leaderboard_endpoint(leaderboard_id: str):
    result = await delete_leaderboard(leaderboard_id)
    if not result:
        raise HTTPException(status_code=404, detail="Leaderboard entry not found")
    return {"detail": "Leaderboard entry deleted successfully"}
