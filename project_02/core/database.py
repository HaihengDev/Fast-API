from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

client = AsyncIOMotorClient(settings.MONGO_URL)

database = client[settings.DB_NAME]

def get_db():
    return database