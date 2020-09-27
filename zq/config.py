import yaml

with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
	if section['db']:
		print("the section is section",section['db'])
		db_name=section['db']['db_name']