from sqlalchemy import String, false, true, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    content: Mapped[str] = mapped_column(String)
   ## owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

class Notelink(Base):
    __tablename__ = "notes_links"
    id = mapped_column(Integer, primary_key=True)
    from_note_id = mapped_column(ForeignKey("notes.id"))
    to_note_id = mapped_column(ForeignKey("notes.id"))