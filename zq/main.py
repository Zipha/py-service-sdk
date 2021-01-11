
from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from . import ALLOWED_HOSTS, API_V1_STR, PROJECT_NAME

# from .core.errors import http_422_error_handler, http_error_handler
from .db.mongodb_utils import close_mongo_connection, connect_to_mongo

app = FastAPI(title=PROJECT_NAME)

if not ALLOWED_HOSTS:
	   ALLOWED_HOSTS = ["http://thezipha.com/","http://www.thezipha.com/","https://thezipha.com/","https://www.thezipha.com/","http://35.190.15.220/","http://localhost:3001/","http://localhost:3000/","http://localhost:3002/"]

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


