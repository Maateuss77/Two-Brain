from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    username: str
    password: str

    class Config:
        from_attributes = True

class UserRead(BaseModel):
    id: int
    name: str
    username: str
    avatar_url: Optional[str]

    class Config:
        from_attributes = True