from .base import DBModelMixin


class TokenPayload(DBModelMixin):
	'''classs token model'''
	account_id: str = ""