from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session 
from typing import List 
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate
from app.schemas.user import UserLogin
from app.schemas.user import UserResponse
from app.auth.utils import verify_password
from app.auth.utils import create_access_token
from app.auth.utils import hash_password
router = APIRouter()

@router.post("/users/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    
    nuevo = User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
    


@router.post ("/user", response_model = UserCreate)
    
    
#endpoint login
@router.post("/users/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == form_data.username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    token = create_access_token(data={"sub": str(db_user.id)})
    return {"access_token": token, "token_type": "bearer"}


        