from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from core.connection import get_session
from .models import Movimiento

router = APIRouter()

@router.get("/movimientos/{dni}", summary="Obtener los movimientos por DNI")
def get_movimientos_by_dni(dni: str, session: Session = Depends(get_session)):
    movimientos = session.exec(select(Movimiento).where(Movimiento.dni == dni)).all()
    
    return {
        "length": len(movimientos),
        "data": [
            {
              **mov.model_dump(),
              "dependencia": mov.dependencia_rel.descripcion if mov.dependencia_rel else None,
              "funcion": mov.funcion_rel.descripcion if mov.funcion_rel else None,
              "vinculo": mov.vinculo_rel.vinculo if mov.vinculo_rel else None
            } 
            for mov in movimientos
        ]
    }