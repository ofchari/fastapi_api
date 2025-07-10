from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.hari_fastapi  # change your_db_name to your choice

user_collection = database.get_collection("users")
log_collection = database.get_collection("logs")
form_collection = database.get_collection("forms")
dashboard_collection = database.get_collection("dashboard")
