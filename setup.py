from setuptools import setup, find_packages

setup(
    name="python-project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.104.0",
        "pydantic>=2.4.2",
        "uvicorn>=0.24.0",
        "sqlalchemy>=2.0.0",
    ],
) 