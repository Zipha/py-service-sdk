from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from ..core.security import generate_salt, get_password_hash, verify_password
class DBModelMixin(BaseModel):
    ''' base class for all the data classes'''
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class AccountLogin(BaseModel):
    '''model class to login the user'''
    login_type:str
    email:Optional[EmailStr]
    password:Optional[str]
    token:Optional[str]
     

class UserBase(BaseModel):
    ''' 
    This class is used to define the user
    '''
    email:EmailStr
    password:Optional[str]
    first_name:str
    last_name:Optional[str]
    phone:Optional[str]
    account_type:str
    signup_type:str="Zipha"
    account_details:Optional[dict]
    is_super_user : bool = False
    user_id:Optional[str] = ''


class AccountBase(UserBase):
    '''
    This class is used to create the Account User
    '''
    account_id:str = ''
    is_active : bool = True
    email_verified: bool = False
    last_visited: datetime = None


class Account(BaseModel):
    '''default account data in get'''
    account_id:str = ''
    user_id:Optional[str] = ''
    email:EmailStr
    first_name:str
    last_name:Optional[str]
    phone:Optional[str]
    account_type:str
    signup_type:str="Zipha"
    account_details:Optional[dict]
    is_super_user : bool = False
    user_id:Optional[str] = ''



class AccountInDB(DBModelMixin, AccountBase):
    ''' This class is used to store in the DB '''
    
    
    salt: str = ''


    def check_password(self, password: str):
        ''' method to check the password '''
        return verify_password(self.salt + password, self.password)

    def change_password(self, password: str):
        ''' method to hash the password'''
        self.salt = generate_salt()
        self.password = get_password_hash(self.salt + password)



    