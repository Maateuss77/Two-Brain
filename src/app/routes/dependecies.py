from app.database.db import Session

def session_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()