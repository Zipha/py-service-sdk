import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zq",
    version="0.0.2",
    author="Zipha",
    author_email="admin.zipha@thezipha.com",
    description="zipha base package ",
    long_description=long_description,
    url="https://github.com/Zipha/py-service-sdk",
    packages=setuptools.find_packages(include=['fastapi','fastapi.*','uvicorn', 
                                            'uvicorn.*','motor','motor.*','pydantic','pydantic.*','starlette','starlette.*',
                                            'zq','zq.*','typing','typing.*','datetime','datetime.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['fastapi','uvicorn','motor','pyyaml','itsdangerous','redis','databases','dataclasses','bcrypt','jwt','pyjwt','passlib',' pydantic[email]']
)
