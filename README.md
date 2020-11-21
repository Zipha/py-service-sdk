Zipha Base Sdk / Package

1. setup.py
	a. All the dependencies for the package has been defined.
	b. The package information also has been defined.

2. zp(actual code folder)
	a. zp.api.api file defines the router which will be used in each services to register service level endpoints.
	b. core.config file defines following.
		1. SECRET_KEY & SECRET_SALT : used for token creation and verification of email, reset password and acces token.
		2. EMAIL_VERIFY_TOKEN_EXPIRE_MINUTES & RESET_PASSWORD_TOKEN_EXPIRE_MINUTES:  expiry durations of tokens for email verification and password  reset.
	c. core.jwt:  file is used to generate and validate user access tokens.

	d. core.permission: file is used to define permission classes.

	e. zp.utils: contains classes and functions of general utility used in multiple places throughout different services.

	f. db folder:  defines the configuration information  and connections for service level databases to run.

	g. models defines base db models used in different services.

3. to create a new version of the packages.
	a. first  change the package version in setup.py.

	b. cd to your repository folder .

	c. make sure you have installed python in your system. 

	d . finally run the "python setup.py sdist" : it will create a folder called dist and stores the package file with .tar.gz extention inside it ex: dist/zq-0.0.1.tar.gz
 
4. to create package.
	-clone the sdk repository.
	- changedirectory (cd) into repository.
	- make sure you have python installed in your system.
	- finally run "python setup.py sdist" CMD to create new package (to change the version go to setup.py file change the 	value of  "version" variable). 
	- now new package will be located in "repository_folder/dist" folder .


5. to install package on local machine
	- open the dist folder under sdk repository folder.
	- copy the file with .tar.gz extension into targeted folder.
	- finally run "pip install sample-0.0.1.tar.gz "   this will install  zipha sdk to targeted env.

