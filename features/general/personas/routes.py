from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from core.connection import get_session
from .models import Persona

router = APIRouter()

@router.get("/personas", summary="Obtener personas")
def get_personas(limit: int = 10, session: Session = Depends(get_session)):
    personas = session.exec(select(Persona).limit(limit)).all()
    return {"length": len(personas), "data": personas}

@router.get("/persona/{dni}", summary="Obtener persona por dni")
def get_person_by_dni(dni: str, session: Session = Depends(get_session)):
    persona = session.exec(select(Persona).where(Persona.dni == dni)).first()
    return {"data": persona}