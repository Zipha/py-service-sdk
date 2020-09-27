import yaml
import os

with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)


if cfg['db']:
	db = cfg['db']MONGO_HOST

	MAX_CONNECTIONS_COUNT = db['MAX_CONNECTIONS_COUNT']
	MIN_CONNECTIONS_COUNT = db['MIN_CONNECTIONS_COUNT']
	MONGO_HOST =  db['MONGO_HOST']
	MONGO_PORT = db['MONGO_PORT']
	MONGO_USER = db['MONGO_USER']
	MONGO_PASS = db['MONGO_PASS']
	MONGO_DB = db['MONGO_DB']
if cfg['project']:
	project = cfg['project']
	API_V1_STR = project['API_V1_STR']
	JWT_TOKEN_PREFIX = project['JWT_TOKEN_PREFIX']
	PROJECT_NAME = project["PROJECT_NAME"]
	ALLOWED_HOSTS =  project["ALLOWED_HOSTS"]
		
