from fastapi import APIRouter, UploadFile, File
from services.food_processing import process_food_image

router = APIRouter()

@router.post("/api/food_recognition")
def recognize_food(file: UploadFile = File(...)):
    return process_food_image(file)
