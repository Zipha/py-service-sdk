
from databases import DatabaseURL
from ..import MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT, MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASS, MONGO_DB

'''
config file to  declare the information needed for db connections

'''



# MAX_CONNECTIONS_COUNT = 10
# MIN_CONNECTIONS_COUNT = 10
# MONGO_HOST = "127.0.0.1"
# MONGO_PORT = 27017
# MONGO_USER = "mongo-admin"
# MONGO_PASS =  "superuser"
# MONGO_DB = "account_service"

MONGODB_URL = DatabaseURL(
        f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    )


database_name = MONGO_DB
account_collection_name="account"

