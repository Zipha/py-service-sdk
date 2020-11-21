from itsdangerous import URLSafeTimedSerializer
from .config import SECRET_KEY, SECRET_SALT, EMAIL_VERIFY_TOKEN_EXPIRE_MINUTES, RESET_PASSWORD_TOKEN_EXPIRE_MINUTES

def generate_confirmation_token(account_id):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    return serializer.dumps(account_id, salt=SECRET_SALT)


def confirm_email_token(token, expiration=EMAIL_VERIFY_TOKEN_EXPIRE_MINUTES):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    try:
        account_id = serializer.loads(
            token,
            salt=SECRET_SALT,
            max_age=expiration
        )
    except:
        return False
    return account_id

def confirm_password_reset_token(token, expiration=RESET_PASSWORD_TOKEN_EXPIRE_MINUTES):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    try:
        account_id = serializer.loads(
            token,
            salt=SECRET_SALT,
            max_age=expiration
        )
    except:
        return False
    return account_id