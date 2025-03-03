from setuptools import setup, find_packages

setup(
    name="people-service",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.68.0",
        "sqlalchemy==1.4.0",
        "pydantic==1.8.2",
        "uvicorn==0.15.0",
        "python-dotenv==0.19.0"
    ],
    extras_require={
        "test": [
            "pytest==7.4.3",
            "pytest-asyncio==0.21.1",
            "httpx==0.24.1"
        ]
    }
) 