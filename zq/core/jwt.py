from datetime import datetime, timedelta
from typing import Optional

import jwt
from fastapi import Depends, Header
from starlette.exceptions import HTTPException
from starlette.status import HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED

from ..db.mongodb import AsyncIOMotorClient, get_database
from ..models.token import TokenPayload
from .config import SECRET_KEY
import logging
from ..rediscache.redis_setup  import client  
from ..rediscache.rediscache import get_routes_from_cache, set_routes_to_cache
import json
ALGORITHM = "HS256"
access_token_jwt_subject = "access"
from .config import candidate_account_type,institution_account_type,expert_account_type,mentor_account_type



def _get_authorization_token(authorization: str = Header(...)):
   
    token = authorization
    # if token_prefix != JWT_TOKEN_PREFIX:
    #     raise HTTPException(
    #         status_code=HTTP_403_FORBIDDEN, detail="Invalid authorization type"
    #     )

    return token


async def _get_current_user(
    db: AsyncIOMotorClient = Depends(get_database),token: str = Depends(_get_authorization_token)
) :
    '''function that decodes the authorization token and retrives the current active user'''
    try:
        payload = jwt.decode(token, str(SECRET_KEY), algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    return token_data

async def _get_current_candidate(
    db: AsyncIOMotorClient = Depends(get_database),token: str = Depends(_get_authorization_token)
) :
    '''function that decodes the authorization token and retrives the current active user'''
    try:
        payload = jwt.decode(token, str(SECRET_KEY), algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    if token_data.account_type == candidate_account_type:
        return token_data
    else:
         raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Not Authoried"
        )

async def _get_current_institution(
    db: AsyncIOMotorClient = Depends(get_database),token: str = Depends(_get_authorization_token)
) :
    '''function that decodes the authorization token and retrives the current active user'''
    try:
        payload = jwt.decode(token, str(SECRET_KEY), algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    print("the token data",token_data)
    if token_data.account_type == institution_account_type:
        return token_data
    else:
         raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Not Authoried"
        )

async def _get_current_superuser(
    db: AsyncIOMotorClient = Depends(get_database),token: str = Depends(_get_authorization_token)
) :
    '''function that decodes the authorization token and retrives the current active user'''
    try:
        payload = jwt.decode(token, str(SECRET_KEY), algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    if token_data.is_super_user:
        return token_data
    else:
         raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Not Authoried"
        )
    

    # dbuser = await get_account(db, token_data.account_id)
    # if not dbuser:
    #     raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    # user = Account(**dbuser.dict())
    # logging.info(f'user is {user}')
    # return user


async def _get_current_active_user(
    db: AsyncIOMotorClient = Depends(get_database), token: str = Depends(_get_authorization_token)
):              
    '''function that decodes the authorization token and retrives the current active user'''
    try:
        payload = jwt.decode(token, str(SECRET_KEY), algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    return token_data.account_id







def _get_authorization_token_optional(authorization: str = Header(None)):
    if authorization:
        return _get_authorization_token(authorization)
    return ""


async def _get_current_user_optional(
    db: AsyncIOMotorClient = Depends(get_database),
    token: str = Depends(_get_authorization_token_optional),
) :
    if token:
        return await _get_current_user(db, token)

    return None


def get_current_user_authorizer(*, required: bool = True):
    '''get current user autherization'''
    if required:
        return _get_current_user
    else:
        return _get_current_user_optional



        return _get_current_user_optional


def get_current_candidate_authorizer(*, required: bool = True):
    '''get current user autherization'''
    if required:
        return _get_current_candidate
    else:
        return _get_current_user_optional

def get_current_institution_authorizer(*, required: bool = True):
    '''get current user autherization'''
    if required:
        return _get_current_institution
    else:
        return _get_current_user_optional


def get_current_super_user_authorizer(*, required: bool = True):
    '''get current user autherization'''
    if required:
        return _get_current_superuser
    else:
        return _get_current_user_optional



def create_access_token(*, data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire, "sub": access_token_jwt_subject})
    encoded_jwt = jwt.encode(to_encode, str(SECRET_KEY), algorithm=ALGORITHM)
    return encoded_jwt
