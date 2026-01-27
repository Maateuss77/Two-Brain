import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.base import Base
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = str(os.getenv("DATABASE_URL"))
db = create_engine(DATABASE_URL, echo=True)
Session  = sessionmaker(bind=db)