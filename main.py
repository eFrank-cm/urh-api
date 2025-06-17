from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from core.connection import get_session
from personal.vinculos.models import Vinculo
from personal.funciones.models import Funcion
from personal.personas.routes import router as personal_router

app = FastAPI()

app.include_router(personal_router, prefix="/personal", tags=["Personal"])

@app.get("/vinculos")
def get_vinculos(limit: int = 10, session: Session = Depends(get_session)):
    vinculos = session.exec(select(Vinculo).limit(limit)).all()
    return {"length": len(vinculos), "data": vinculos}

@app.get("/funciones")
def get_funciones(limit: int=10, session: Session = Depends(get_session)):
    funciones = session.exec(select(Funcion).limit(limit)).all()
    return {"length": len(funciones), "data": funciones}

@app.get("/vinculos-detalle")
def get_vinculos(limit: int = 10, session: Session = Depends(get_session)):
    result = session.exec(select(Vinculo).limit(limit)).all()
    return [
        {
            **v.model_dump(),
            "dependencia": v.dependencia_rel.descripcion if v.dependencia_rel else None,
            "funcion": v.funcion_rel.descripcion if v.funcion_rel else None
        }
        for v in result
    ]

