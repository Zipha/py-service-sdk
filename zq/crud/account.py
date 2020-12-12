from zq.db.mongodb import AsyncIOMotorClient
from pydantic import EmailStr
from typing import Optional,List
from bson.objectid import ObjectId
from datetime import datetime
from ..db.db_config import database_name ,account_collection_name
from ..models.account import AccountCreate, AccountGet, AccountUpdate, AccountDelete, AccountInDB, Account
import logging
from typing import List



async def get_account(conn: AsyncIOMotorClient, account_id: str) -> List[AccountInDB]:
	'''function to get account with account_id'''
	row = await conn[database_name][account_collection_name].find_one({"account_id": account_id})
	if row:
		# print(row)
		return AccountInDB(**row)

async def get_account_list(conn: AsyncIOMotorClient,limit: Optional[int] = 20, offset:Optional[ int] = 0,):
	'''function to get account list '''
	row_object =  conn[database_name][account_collection_name].find(limit=limit,
                                                             skip=offset)
	accounts: List[AccountGet] = []
	async for row in row_object:
		accounts.append(
            AccountGet(account=Account(**row,)

            	)
            )

	return accounts 

async def get_account_by_user_id(conn: AsyncIOMotorClient, user_id: str) -> AccountInDB:
	'''function to get account  by user_id'''
	row = await conn[database_name][account_collection_name].find_one({"user_id": user_id})
	if row:
		return AccountInDB(**row)

async def get_account_by_email(conn: AsyncIOMotorClient, email: EmailStr) -> AccountInDB:
	'''function to get account by email'''
	row = await conn[database_name][account_collection_name].find_one({"email": email})
	if row:
		return AccountInDB(**row)


async def create_user(conn: AsyncIOMotorClient, account: AccountCreate) -> AccountInDB:
	'''function to creat nwe account'''
	dbaccount = AccountInDB(**account.dict())
	dbaccount.created_at = datetime.now()
	dbaccount.updated_at = datetime.now()
	dbaccount.change_password(account.password)
	row = await conn[database_name][account_collection_name].insert_one(dbaccount.dict())
	account_id = str(row.inserted_id)
	dbaccount.account_id= account_id
	updated_at = await conn[database_name][account_collection_name].update_one({"email": dbaccount.email}, {'$set': dbaccount.dict()})
	return dbaccount


async def update_user(conn: AsyncIOMotorClient, account_id: str, user: AccountUpdate) -> AccountInDB:
	'''function to update account'''
	dbuser = await get_account(conn, account_id)
	if  user.password:
		dbuser.change_password(user.password)
	if user.first_name:
		dbuser.first_name = user.first_name
	if user.last_name:
		dbuser.last_name = user.last_name
	if  user.phone:
		dbuser.phone = user.phone
	if user.last_visited:
		dbuser.last_visited = user.last_visited
	if user.is_active:
		dbuser.is_active = user.is_active
	updated_at = await conn[database_name][account_collection_name].update_one({"account_id": account_id}, {'$set': dbuser.dict()})
	dbuser = await get_account(conn, account_id)
	return dbuser



async def delete_user(conn: AsyncIOMotorClient, account_id: str) -> AccountInDB:
	'''function to delete account'''
	dbuser = await get_account(conn, account_id)
	pass

async def email_verify(conn: AsyncIOMotorClient, account_id: str) -> AccountInDB:
	'''function to verify email'''
	updated_at = await conn[database_name][account_collection_name].update_one({"account_id": account_id}, {'$set':{'email_verified':True} })
	dbuser = await get_account(conn, account_id)
	return dbuser






