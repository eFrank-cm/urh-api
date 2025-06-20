from fastapi import APIRouter
from .dependencias.models import Dependencia
from .funciones.models import Funcion
from .personas.models import Persona
from .personas.routes import router as router_persona

Dependencia.model_rebuild()
Funcion.model_rebuild()
Persona.model_rebuild()

router = APIRouter()

router.include_router(router_persona)
