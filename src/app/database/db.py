from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///database.db"

db = create_engine(DATABASE_URL, echo=True)
Session  = sessionmaker(bind=db)