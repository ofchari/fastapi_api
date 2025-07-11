from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_DETAILS = os.getenv("MONGO_DETAILS")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.hari_fastapi  # change your_db_name to your choice

user_collection = database.get_collection("users")
log_collection = database.get_collection("logs")
form_collection = database.get_collection("forms")
dashboard_collection = database.get_collection("dashboard")
