from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import TEXT, Boolean, String, ForeignKey, CheckConstraint, UniqueConstraint, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base

if TYPE_CHECKING:
    from .User import User

class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(TEXT)
    is_delete: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    date_create: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now(), 
        nullable=False
    ) 
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    owner: Mapped["User"] = relationship("User",back_populates="notes")

class NoteLink(Base):
    __tablename__ = "notes_links"

    id: Mapped[int] = mapped_column(primary_key=True)

    from_note_id: Mapped[int] = mapped_column(ForeignKey("notes.id",ondelete="CASCADE"), nullable=False)
    to_note_id: Mapped[int] = mapped_column(ForeignKey("notes.id",ondelete="CASCADE"), nullable=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    __table_args__ = (CheckConstraint("from_note_id != to_note_id"),UniqueConstraint("from_note_id", "to_note_id"))