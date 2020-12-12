import bcrypt
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




def generate_salt():
	'''function to generate the salt for hashing password'''
	return bcrypt.gensalt().decode()


def verify_password(plain_password, hashed_password):
	'''function to verify the password'''
	return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
	'''function to ash the password'''
	return pwd_context.hash(password)

