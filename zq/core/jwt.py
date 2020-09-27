from datetime import datetime, timedelta
from typing import Optional

import jwt
from fastapi import Depends, Header
from jwt import PyJWTError
from starlette.exceptions import HTTPException
from starlette.status import HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED
from .config import  SECRET_KEY
from ..models.token import TokenPayload


ALGORITHM = "HS256"
access_token_jwt_subject = "access"


def _get_authorization_token(authorization: str = Header(...)):
   
    token = authorization
    # if token_prefix != JWT_TOKEN_PREFIX:
    #     raise HTTPException(
    #         status_code=HTTP_403_FORBIDDEN, detail="Invalid authorization type"
    #     )

    return token


async def validate_token(
   token: str = Depends(_get_authorization_token)):
    '''function that decodes the autherise token '''
    try:
        payload = jwt.decode(token, str(SECRET_KEY), algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    return token_data