from setuptools import setup, find_packages

setup(
    name="python-project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.95.2",
        "pydantic==1.10.7",
        "uvicorn==0.22.0",
        "sqlalchemy==2.0.23",
        "python-dotenv==0.19.0",
        "python-multipart==0.0.6",
        "email-validator==2.0.0",
        "pytest==7.4.0",
        "httpx==0.24.0",
        "pytest-asyncio==0.21.0",
        "pytest-cov==4.1.0"
    ],
) 