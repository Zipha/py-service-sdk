
from motor.motor_asyncio import AsyncIOMotorClient
from .db_config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from .mongodb import db
import logging

'''
file to get connection to db and close connection with db 
'''

'''
*
*************************************************************************
* QUANSCENDENCE CONFIDENTIAL
* __________________________
*
*  [2020] - [*] Quanscendence Technologies Private Limited
*  All Rights Reserved.
*
* NOTICE:  All information contained herein is, and remains
* the property of Quanscendence Technologies Private Limited (Quanscendence).
* The code has been developed for Zipha Technologies Private Limited (Zipha)
* and abides to the consulting agreement between Quanscendence and Zipha
* mutually approved and signed during June 2020.
*
* The intellectual and technical concepts contained
* herein are proprietary to Quanscendence Technologies Private Limited
* and its suppliers and may be covered by India, U.S. and Foreign Patents,
* patents in process, and are protected by trade secret or copyright law.
* Dissemination of this information or reproduction of this material
* is strictly forbidden unless prior written permission is obtained
* from Quanscendence Technologies Private Limited.
*************************************************************************
''' 

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





