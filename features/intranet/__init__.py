from fastapi import APIRouter
from .usuario.models import Usuario
from .usuario.routes import router as router_usuarios

Usuario.model_rebuild()

router = APIRouter()

router.include_router(router_usuarios)