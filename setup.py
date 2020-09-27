import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zq",
    version="0.0.1",
    author="vishwa",
    author_email="vishwa@quasnscendence.com",
    description="zipha base package ",
    long_description=long_description,
    url="https://github.com//ziphasdk",
    packages=setuptools.find_packages(include=['fastapi','fastapi.*','uvicorn', 
                                            'uvicorn.*','motor','motor.*','pydantic','pydantic.*','starlette','starlette.*',
                                            'zq','zq.*','typing','typing.*','datetime','datetime.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['fastapi','uvicorn','motor','pyyaml','itsdangerous']
)