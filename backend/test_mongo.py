from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from routes import users, meals, nutrition, goals, leaderboard

app = FastAPI(title="Vittaly API")

# Mount the static directory (contains your api_docs.html as index.html)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Include API routes under their own prefixes
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(meals.router, prefix="/api/meals", tags=["Meals"])
app.include_router(nutrition.router, prefix="/api/nutrition", tags=["Nutrition"])
app.include_router(goals.router, prefix="/api/goals", tags=["Goals"])
app.include_router(leaderboard.router, prefix="/api/leaderboard", tags=["Leaderboard"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    
