from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    username: str
    password: str
    image: str
    class Config:
        from_attributes = True

class UserRead(BaseModel):
    id: int
    name: str
    username: str
    image: str

    class Config:
        from_attributes = True