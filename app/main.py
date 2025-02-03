import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from app.core.config import settings
from app.api.route.route import router

def init_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router, prefix="/api")
    app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)
    return app


app = init_app()
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8002)