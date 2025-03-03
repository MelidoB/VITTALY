from fastapi import APIRouter, HTTPException
from models.user import User
from services.user_service import (
    add_new_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)

router = APIRouter()

@router.post("/", response_model=dict)
async def create_user(user: User):
    result = await add_new_user(user.model_dump())
    if isinstance(result, dict) and "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return {"user_id": result}

@router.get("/", response_model=list[User])
async def list_users():
    return await get_all_users()

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: str):
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
async def update_user_endpoint(user_id: str, user: User):
    updated = await update_user(user_id, user.model_dump())
    if updated is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}", response_model=dict)
async def delete_user_endpoint(user_id: str):
    result = await delete_user(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
