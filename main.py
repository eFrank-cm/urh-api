from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from db.connection import get_session
from personal.models.persona import Persona
from personal.models.vinculo import Vinculo

app = FastAPI()

@app.get("/personal")
def get_personal(limit: int = 10, session: Session = Depends(get_session)):
    personas = session.exec(select(Persona).limit(limit)).all()
    return {"length": len(personas), "data": personas}

@app.get("/vinculos")
def get_vinculos(limit: int = 10, session: Session = Depends(get_session)):
    vinculos = session.exec(select(Vinculo).limit(limit)).all()
    return {"length": len(vinculos), "data": vinculos}

@app.get("/vinculos-con-dependencia")
def get_vinculos(session: Session = Depends(get_session)):
    result = session.exec(select(Vinculo).limit(10)).all()
    return [
        {
            **v.model_dump(),
            "dependencia": v.dependencia_rel.descripcion if v.dependencia_rel else None
        }
        for v in result
    ]

