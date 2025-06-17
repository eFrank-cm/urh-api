from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from core.connection import get_session
from general.funciones.models import Funcion

router = APIRouter()

@router.get("/funciones", summary="Obtener Funciones")
def get_funciones(limit: int = 10, session: Session = Depends(get_session)):
    funciones = session.exec(select(Funcion).limit(limit)).all()
    return {"length": len(funciones), "data": funciones}