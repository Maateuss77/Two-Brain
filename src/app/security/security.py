from pwdlib import PasswordHash
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from jose import jwt
from datetime import datetime, timedelta, timezone

pwd_context = PasswordHash.recommended()

def pwd_hash(password:str):
    return pwd_context.hash(password)

def verify_hash(pwd_normal : str, hash : str):
    return pwd_context.verify(pwd_normal, hash)

def create_acess_token(subject : str, expire_time: timedelta | None = None):
    now = datetime.now(timezone.utc)
    expire =   + (expire_time or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    payload = {
        "sub": subject,
        "exp": expire,
        "iat": now
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
