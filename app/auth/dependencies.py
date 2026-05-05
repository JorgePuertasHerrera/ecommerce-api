from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session 
from jose import JWTError 
from app.database import get_db 
from app.models.user import User 
from app.auth.utils import decode_token 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_current_user(token:str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = decode_token(token)
        user_id =payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail= "Token inválido")
    except JWTError:
        raise HTTPException(status_code= 401, detail= "Token inválido")
    user= db.query(User).get(int(user_id))
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    return user