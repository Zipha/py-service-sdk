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
from fastapi import APIRouter, Body, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from datetime import timedelta
from ....core.config import ACCESS_TOKEN_EXPIRE_MINUTES, EMAIL_VERIFY_TOKEN_EXPIRE_MINUTES, RESET_PASSWORD_TOKEN_EXPIRE_MINUTES
from ....core.jwt import create_access_token,get_current_user_authorizer
from ....crud.account import get_account,get_account_by_email








