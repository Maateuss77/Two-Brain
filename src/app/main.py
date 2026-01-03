from fastapi import FastAPI
import uvicorn
from app.routes.auth_route import auth_routes
from app.routes.note_route import note_route
from app.database.db import db

app = FastAPI(title="Two brain api")
app.include_router(auth_routes)
app.include_router(note_route)


def run():
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )