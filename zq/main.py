
from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


from . import ALLOWED_HOSTS, API_V1_STR, PROJECT_NAME
# from .core.errors import http_422_error_handler, http_error_handler
from .db.mongodb_utils import close_mongo_connection, connect_to_mongo

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

app = FastAPI(title=PROJECT_NAME)

if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

# app.add_exception_handler(HTTPException, http_error_handler)
# app.add_exception_handler(HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler)


