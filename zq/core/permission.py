from starlette.status import HTTP_403_FORBIDDEN, HTTP_401_UNAUTHORIZED
from starlette.exceptions import HTTPException

def permission_to_get_account(dbuser,current_user):
	'''funtion to check the user to get the requested information'''
	if current_user.account_id == dbuser.account_id:
		return True
	elif  'Admin' in current_user.role or 'Employer'in current_user.role:
		return True
	else:
		raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED, detail="Account not Autherized to Access"
        )

