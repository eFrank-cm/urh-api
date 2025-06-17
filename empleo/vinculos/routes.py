from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from core.connection import get_session
from empleo.vinculos.models import Vinculo

router = APIRouter()

@router.get("/vinculos", summary="Obtiene los vinculos")
def get_vinculos(limit: int = 10, session: Session = Depends(get_session)):
    vinculos = session.exec(select(Vinculo).limit(limit)).all()
    return {
        "length": len(vinculos),
        "data": [
            {
                **v.model_dump(),
                "dependencia": v.dependencia_rel.descripcion if v.dependencia_rel else None,
                "funcion": v.funcion_rel.descripcion if v.funcion_rel else None,
                "nombres": v.dni_rel.nombres if v.dni_rel else None
            }
            for v in vinculos
        ]
    }

@router.get("/vinculos/{dni}", summary="")
def get_vinculos_by_dni(dni: str, session: Session = Depends(get_session)):
    vinculos = session.exec(select(Vinculo).where(Vinculo.dni == dni)).all()
    return {
        "length": len(vinculos), 
        "data": [
            {
                **v.model_dump(),
                "dependencia": v.dependencia_rel.descripcion if v.dependencia_rel else None,
                "funcion": v.funcion_rel.descripcion if v.funcion_rel else None,
                "nombres": v.dni_rel.nombres if v.dni_rel else None
            }
            for v in vinculos
        ]
    }