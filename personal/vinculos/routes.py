from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from core.connection import get_session
from personal.personas.models import Persona

router = APIRouter()

@router.get("/vinculos", summary="Obtener vinculos")
def get_personas(limit: int = 10, session: Session = Depends(get_session)):
    personas = session.exec(select(Persona).limit(limit)).all()
    return {"length": len(personas), "data": personas}