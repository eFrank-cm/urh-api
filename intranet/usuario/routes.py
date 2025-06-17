from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from core.connection import get_session
from intranet.usuario.models import Usuario
import hashlib

router = APIRouter()

@router.get("/usuarios", summary="Obtener usuarios")
def get_usuarios(limit:int = 10, session: Session = Depends(get_session)):
    usuarios = session.exec(select(Usuario).limit(limit)).all()
    return {"length": len(usuarios), "data": usuarios}

@router.get("/usuario", summary="Validar usuario")
def get_person_by_dni(dni: str, password: str, session: Session = Depends(get_session)):
    hashed_pass = hashlib.md5(password.encode()).hexdigest()
    usuario = session.exec(select(Usuario).where((Usuario.dni == dni) & (Usuario.password == hashed_pass))).first()
    return {"data": {
        **usuario.model_dump(),
        "nombres": usuario.persona_rel.nombres if usuario.persona_rel else None,
        "email": usuario.persona_rel.email if usuario.persona_rel else None
    }}