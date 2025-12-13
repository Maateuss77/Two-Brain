from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session

from app.database.schemas.userSchema import UserCreate
from app.routes.dependecies import session_db
from app.database.model.userModel import User
from app.security.cryptography import pwd_hash, verify_hash

auth_routes = APIRouter(prefix="/Auth")

@auth_routes.post("/create", tags=["sign"])
async def create_user(schema: UserCreate, session: Session = Depends(session_db)):

    user = session.query(User).filter(User.username == schema.username).first()

    if user:
        raise HTTPException(status_code=400, detail="User exist in DATABASE")
    else:
        password_cript = pwd_hash(schema.password)
        new_user = User(name = schema.name, username = schema.username, password = password_cript)
        session.add(new_user)
        session.commit()
        raise HTTPException(status_code=200, detail="Success create user!")