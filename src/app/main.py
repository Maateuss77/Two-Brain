from fastapi import FastAPI
import uvicorn
from app.routes.user_routes import auth_routes
from app.database.db import db
app = FastAPI(title="Two brain api")
app.include_router(auth_routes)


def run():
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )