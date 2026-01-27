from app.database.db import db
from sqlalchemy import text

def test_database_connection():
    with db.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        assert result.scalar() == 1
