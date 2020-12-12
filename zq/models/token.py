from .base import DBModelMixin


class TokenPayload(DBModelMixin):
	'''classs token model'''
	account_id: str = ""
	signup_type:str
	is_active : bool
	is_super_user : bool
	account_type:str