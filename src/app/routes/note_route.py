from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from sqlalchemy import or_, and_
from app.database.model.Note import Note, NoteLink
from app.database.model.User import User
from app.database.schemas.Note import NoteCreate, NoteUpdate
from app.routes.dependecies import session_db
from app.routes.auth_route import get_current_user
from app.routes.dependecies import session_db

note_route = APIRouter(prefix="/Note")

@note_route.post("/create", tags=["Note"])
async def create_note(schema : NoteCreate ,session : Session = Depends(session_db), user: User = Depends(get_current_user)):
    note = Note(title=schema.title, content=schema.content, owner_id=user.id, delete=False)
    session.add(note)
    session.commit()
    session.refresh(note)
    return note

@note_route.get("/", tags=["Note"])
async def get_all_notes(session : Session = Depends(session_db), user: User = Depends(get_current_user)):
    return (session.query(Note).filter(Note.owner_id == user.id).all())

@note_route.put("/{note_id}", tags=["Note"])
async def update_note(
    note_id: int,
    schema: NoteUpdate,
    session: Session = Depends(session_db),
    user: User = Depends(get_current_user),
):
    note = (
        session.query(Note)
        .filter(
            Note.id == note_id,
            Note.owner_id == user.id
        )
        .first()
    )

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    if schema.title is not None:
        note.title = schema.title

    if schema.content is not None:
        note.content = schema.content

    if schema.connections is not None:
        session.query(NoteLink).filter(
            NoteLink.from_note_id == note_id,
            NoteLink.owner_id == user.id
        ).delete()
        for target_id in schema.connections:
            link = NoteLink(
                from_note_id=note_id,
                to_note_id=target_id,
                owner_id=user.id
            )
            session.add(link)

    session.commit()
    session.refresh(note)

    return note

@note_route.delete("/{note_id}", tags=["Note"])
async def delete_note(note_id: int, session: Session = Depends(session_db), user: User = Depends(get_current_user)):
    note = session.query(Note).filter(Note.id == note_id).first
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    session.delete(note)
    session.commit()
    return {"detail": "Note deleted successfully"}

@note_route.post("/{from_id}/link/{to_id}", tags=["Note"])
async def link_notes(
    from_id: int,
    to_id: int,
    session: Session = Depends(session_db),
    user: User = Depends(get_current_user)
):
    notes = session.query(Note).filter(
        Note.id.in_([from_id, to_id]),
        Note.owner_id == user.id
    ).all()

    if len(notes) != 2:
        raise HTTPException(status_code=404)

    link = NoteLink(
        from_note_id=from_id,
        to_note_id=to_id,
        owner_id=user.id
    )

    session.add(link)
    session.commit()
    return {"ok": True}

@note_route.get("/{note_id}/connections", tags=["Note"])
async def get_note_connections(
    note_id: int,
    session: Session = Depends(session_db),
    user: User = Depends(get_current_user),
):
    note = (session.query(Note).filter(Note.id == note_id,Note.owner_id == user.id).first())

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    connections = (session.query(Note).join(NoteLink,or_(
                NoteLink.from_note_id == Note.id,
                NoteLink.to_note_id == Note.id,
            )
        )
        .filter(
            or_(
                and_(
                    NoteLink.from_note_id == note.id,
                    NoteLink.to_note_id == Note.id,
                ),
                and_(
                    NoteLink.to_note_id == note.id,
                    NoteLink.from_note_id == Note.id,
                ),
            ),
            Note.owner_id == user.id,
            Note.id != note.id,
        )
        .all()
    )

    return {
        "note_id": note.id,
        "user": user.username,
        "title": note.title,
        "connections": connections,
    }
