from datetime import timedelta
from math import exp
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from app.database.schemas.User import UserCreate
from app.routes.dependecies import session_db
from app.database.model.User import User
from app.security.security import pwd_hash, verify_hash, create_acess_token

auth_routes = APIRouter(prefix="/Auth")

@auth_routes.post("/create", tags=["User"])
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

@auth_routes.post("/login", tags=["User"])
async def login(
                session: Session = Depends(session_db), 
                form_data: OAuth2PasswordRequestForm = Depends()):
    user = session.query(User).filter(User.username == form_data.username).first()

    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credencials")

    password_hash = user.password

    if not verify_hash(form_data.password, password_hash):
        raise HTTPException(status_code=401, detail="User or password incorrect")

    acess_token = create_acess_token(subject=str(user.id), expire_time=timedelta(minutes=15))
    return {
        "access_token": acess_token,
        "token_type": "bearer"
    }