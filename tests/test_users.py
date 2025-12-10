from app.db.model.userModel import User

def test_create_note(db_session):
    user = User(name="Nome", username="mateusu", email="test@test.com", picture="fotopeixe.png")

    db_session.add(user)
    db_session.commit()

    users = db_session.query(User).all()

    assert len(users) == 1
    assert users[0].name == "Nome"
