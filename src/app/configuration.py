from app.database.base import Base
from app.database.db import db
import uvicorn

def run_database():
    Base.metadata.create_all(bind=db)
