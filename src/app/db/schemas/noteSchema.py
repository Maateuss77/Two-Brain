from pydantic import BaseModel

class Notecreate(BaseModel):
    title: str
    content: str
