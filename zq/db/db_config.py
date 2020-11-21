
from databases import DatabaseURL
from ..import MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT, MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASS, MONGO_DB

'''
config file to  declare the information needed for db connections

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


MAX_CONNECTIONS_COUNT = 10
MIN_CONNECTIONS_COUNT = 10
MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_USER = "mongo-admin"
MONGO_PASS =  "superuser"
MONGO_DB = "account_service"

MONGODB_URL = DatabaseURL(
        f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    )


database_name = MONGO_DB


