from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from app.database.model.Note import Note
from app.database.model.User import User
from app.database.schemas.Note import NoteCreate, NoteLinkOut
from app.routes.dependecies import session_db
from app.routes.auth_route import get_current_user
from app.routes.dependecies import session_db

note_route = APIRouter(prefix="/Note")

@note_route.post("/create", tags=["Note"])
async def create_note(schema : NoteCreate ,session : Session = Depends(session_db), user: User = Depends(get_current_user)):
    note = Note(title=schema.title, content=schema.content, owner_id=user.id)
    session.add(note)
    session.commit()
    session.refresh(note)
    return note

@note_route.get("/", tags=["Note"])
async def get_all_notes(session : Session = Depends(session_db), user: User = Depends(get_current_user)):
    return (session.query(Note).filter(Note.owner_id == user.id).all())