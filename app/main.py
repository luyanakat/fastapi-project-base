import uvicorn
from fastapi import FastAPI
from app.api.route.route import router
from app.core.config import settings

def init_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router, prefix="/api")
    return app


app = init_app()
if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)