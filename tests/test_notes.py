from app.db.model.notesModel import Note

def test_create_note(db_session):
    note = Note(title="Teste", content="conteúdo")

    db_session.add(note)
    db_session.commit()

    notes = db_session.query(Note).all()

    assert len(notes) == 1
    assert notes[0].title == "Teste"
