
from motor.motor_asyncio import AsyncIOMotorClient
from .db_config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from .mongodb import db
import logging

async def connect_to_mongo():
    logging.info("connecting")
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
    logging.info("connected")


async def close_mongo_connection():
    logging.info("closing connection...")
    db.client.close()
    logging.info("connection closed")





