from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import query
from sqlalchemy.orm.session import Session
from app.database.schemas.User import UserCreate
from app.routes.dependecies import session_db
from app.database.model.User import User
from app.security.security import pwd_hash, verify_hash, create_acess_token
from jose import JWTError, jwt
from app.config import SECRET_KEY, ALGORITHM

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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/Auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme), session: Session=Depends(session_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        subject: str | None = payload.get("sub")
        if subject is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = session.query(User).filter(User.id ==int(subject)).first()
    if user is None:
        raise credentials_exception
    return user

@auth_routes.get("/me", tags=["User"])
async def protected(user: str = Depends(get_current_user)):
    return {
        "user": user
    }

@auth_routes.delete("/{user_id}/delete", tags=["User"])
async def delete_user(user_id: int,user: User = Depends(get_current_user), session: Session=Depends(session_db)):
    usuary = session.query(User).filter(User.id == user_id).first()
    if not usuary:
        raise HTTPException(status_code=404, detail="User not found")

    session.delete(usuary)
    session.commit()

    return {"detail": "User deleted successfully"}