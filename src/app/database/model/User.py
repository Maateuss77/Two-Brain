from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import Integer, String, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base

if TYPE_CHECKING:
    from .Note import Note

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255),nullable=False)
    picture: Mapped[str|None] = mapped_column(String, nullable=True)

    date_create: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now(), 
        nullable=False
    ) 
    notes: Mapped[list["Note"]] = relationship("Note",back_populates="owner", cascade="all, delete-orphan")