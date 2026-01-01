from pydantic import BaseModel

class NoteCreate(BaseModel):
    title: str
    content: str

    class Config:
        from_attributes = True

class NoteLinkOut(BaseModel):
    to_note_id: int

    class Config:
        from_attributes = True