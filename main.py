# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI
from app import models, database, routes
import uvicorn
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создаем таблицы
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(routes.router)

if __name__ == "__main__":
    try:
        logger.info("Starting the application...")
        uvicorn.run(
            "main:app",
            host="0.0.0.0",  # Важно: слушаем все интерфейсы
            port=8000,
            reload=False  # В продакшене отключаем автоперезагрузку
        )
    except Exception as e:
        logger.error(f"Error starting application: {e}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
