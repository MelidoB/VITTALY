from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

MONGO_URI = os.getenv("MONGO_URI")

# Create an asynchronous MongoDB client and connect to the database
client = AsyncIOMotorClient(MONGO_URI)
db = client["vittality_db"]
