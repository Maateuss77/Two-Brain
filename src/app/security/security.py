from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()

def pwd_hash(password:str):
    return pwd_context.hash(password)

def verify_hash(pwd_normal : str, hash : str):
    return pwd_context.verify(pwd_normal, hash)
