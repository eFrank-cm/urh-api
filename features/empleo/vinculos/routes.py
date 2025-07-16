from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from core.connection import get_session
from .models import Vinculo
from .services import search_vinculos_activos
from .schemas import ds_vinculo_request

router = APIRouter()

@router.get("/vinculos/{dni}", summary="Obtener vinculos por DNI")
def get_vinculos_by_dni(dni: str, session: Session = Depends(get_session)):
    vinculos = session.exec(select(Vinculo).where(Vinculo.dni == dni)).all()
    vinculos_request = [ds_vinculo_request(v) for v in vinculos]
    return {
        "length": len(vinculos_request), 
        "data": vinculos_request
    }
    
@router.get("/activos", summary="Personal activos")
def get_vinculos_activos(session: Session = Depends(get_session)):
    vinculos = search_vinculos_activos(session)
    vinculos_request = [ds_vinculo_request(v) for v in vinculos]
    return {
        "length": len(vinculos),
        "data": vinculos_request
    }
    
@router.get("/vinculo/{id}", summary="Obtener un vinculo por ID")
def get_vinculo_by_id(id: str, session: Session = Depends(get_session)):
    vinculo = session.exec(select(Vinculo).where(Vinculo.vinculo == id)).first()
    return {"data": ds_vinculo_request(vinculo) if vinculo else None} 
    
