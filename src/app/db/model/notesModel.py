from sqlalchemy import String, ForeignKey, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="notes")

class NoteLink(Base):
    __tablename__ = "notes_links"

    id: Mapped[int] = mapped_column(primary_key=True)

    from_note_id: Mapped[int] = mapped_column(ForeignKey("notes.id"), nullable=False)
    to_note_id: Mapped[int] = mapped_column(ForeignKey("notes.id"), nullable=False)
    __table_args__ = (
        CheckConstraint("from_note_id != to_note_id"),
        UniqueConstraint("from_note_id", "to_note_id"),
    )