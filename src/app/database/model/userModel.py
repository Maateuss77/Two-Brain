from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base
from app.database.model.notesModel import Note


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255),nullable=False)
    picture: Mapped[str|None] = mapped_column(String, nullable=True)
    notes: Mapped[List["Note"]] = relationship(back_populates="owner")