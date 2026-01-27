from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.routes.auth_route import auth_routes
from app.routes.note_route import note_route
from app.database.db import db

app = FastAPI(title="Two brain api")
app.include_router(auth_routes)
app.include_router(note_route)
# Configurar as origens permitidas
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, etc)
    allow_headers=["*"], # Permite todos os headers
)


def run():
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )