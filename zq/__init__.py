import yaml


import os
MAX_CONNECTIONS_COUNT = os.environ['MAX_CONNECTIONS_COUNT']
MIN_CONNECTIONS_COUNT = os.environ['MIN_CONNECTIONS_COUNT']
MONGO_HOST  = os.environ['MONGO_HOST']
MONGO_PORT =os.environ['MONGO_PORT'] 
MONGO_USER =   os.environ['MONGO_USER']
MONGO_PASS  = os.environ['MONGO_PASS']
MONGO_DB= os.environ['MONGO_DB']
API_V1_STR = os.environ['API_V1_STR']
JWT_TOKEN_PREFIX = os.environ['JWT_TOKEN_PREFIX']
PROJECT_NAME = os.environ["PROJECT_NAME"]
ALLOWED_HOSTS =  ["*"]
KAFKA_URL = os.environ["KAFKA_URL"]
REDIS_PORT = os.environ["REDIS_PORT"]
REDIS_HOST = os.environ["REDIS_PORT"]


# with open("config.yml", "r") as ymlfile:
#     cfg = yaml.load(ymlfile)


# if cfg['db']:
# 	db = cfg['db']

# 	MAX_CONNECTIONS_COUNT = db['MAX_CONNECTIONS_COUNT']
# 	MIN_CONNECTIONS_COUNT = db['MIN_CONNECTIONS_COUNT']
# 	MONGO_HOST =  db['MONGO_HOST']
# 	MONGO_PORT = db['MONGO_PORT']
# 	MONGO_USER = db['MONGO_USER']
# 	MONGO_PASS = db['MONGO_PASS']
# 	MONGO_DB = db['MONGO_DB']
# if cfg['project']:
# 	project = cfg['project']
# 	API_V1_STR = project['API_V1_STR']
# 	JWT_TOKEN_PREFIX = project['JWT_TOKEN_PREFIX']
# 	PROJECT_NAME = project["PROJECT_NAME"]
# 	ALLOWED_HOSTS =  project["ALLOWED_HOSTS"]
# if cfg['kafka']:
# 	kafka = cfg['kafka']
# 	KAFKA_URL = kafka['KAFKA_URL']


# if cfg['redis']:
# 	redis = cfg['redis']
# 	REDIS_PORT=redis['REDIS_PORT']
# 	REDIS_HOST = redis['REDIS_HOST']


	