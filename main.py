# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI, Response
import uvicorn
import logging
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from app import models, database, routes
    logger.info("Modules imported successfully")
    
    models.Base.metadata.create_all(bind=database.engine)
    logger.info("Database tables created")
    
    app = FastAPI()
    
    # Добавляем CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.include_router(routes.router)
    logger.info("Router included")
    
    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}
    
    @app.get("/favicon.ico")
    async def favicon():
        return Response(status_code=204)
    
    if __name__ == "__main__":
        logger.info("Starting the application...")
        uvicorn.run(app, host="127.0.0.1", port=8001)
        
except Exception as e:
    logger.error(f"Error during startup: {str(e)}")
    raise

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
