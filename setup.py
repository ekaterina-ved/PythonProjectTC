from setuptools import setup, find_packages

setup(
    name="python-project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.95.2",
        "pydantic==1.10.7",
        "uvicorn==0.22.0",
        "sqlalchemy==1.4.41",
    ],
) 