import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.base import Base
from app.database.model.Note import Note
from app.database.model.Note import User


@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = TestingSessionLocal()
    yield session

    session.close()

def test_create_note(db_session):
    note = Note(title="Teste", content="conteúdo")

    db_session.add(note)
    db_session.commit()

    notes = db_session.query(Note).all()

    assert len(notes) == 1
    assert notes[0].title == "Teste"

def test_create_user(db_session):
    user = User(name="Nome", username="mateusu", password_hash="bucetarosa")

    db_session.add(user)
    db_session.commit()

    users = db_session.query(User).all()

    assert len(users) == 1
    assert users[0].name == "Nome"

