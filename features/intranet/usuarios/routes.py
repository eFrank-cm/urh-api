from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from core.connection import get_session
from .models import Usuario
from .schemas import LoginRequest
from .services import create_access_token
import hashlib

router = APIRouter()

@router.get("/usuarios", summary="Obtener usuarios")
def get_usuarios(limit:int = 10, session: Session = Depends(get_session)):
    usuarios = session.exec(select(Usuario).limit(limit)).all()
    return {"length": len(usuarios), "data": usuarios}

@router.post("/auth", summary="Validar usuario")
def get_person_by_dni(body: LoginRequest, session: Session = Depends(get_session)):
    hashed_pass = hashlib.md5(body.password.encode()).hexdigest()
    usuario = session.exec(select(Usuario).where((Usuario.dni == body.username) & (Usuario.password == hashed_pass))).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    token = create_access_token({"sub": usuario.dni})
    return {"success": True, "detail": "existoso", "token": token}