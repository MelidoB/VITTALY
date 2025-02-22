from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import food_recognition  

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(food_recognition.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Food Recognition API"}
