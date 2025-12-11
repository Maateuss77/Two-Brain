from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    username: str
    password: str
    image: str

class UserRead(BaseModel):
    id: int
    name: str
    email: str
    username: str
    image: str

    class Config:
        from_attributes = True