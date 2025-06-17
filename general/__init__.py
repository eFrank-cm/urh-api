from fastapi import APIRouter
from general.dependencias.models import Dependencia
from general.funciones.models import Funcion
from general.personas.models import Persona
from general.personas.routes import router as router_persona

Dependencia.model_rebuild()
Funcion.model_rebuild()
Persona.model_rebuild()

router = APIRouter()

router.include_router(router_persona, tags=["Persona"])
