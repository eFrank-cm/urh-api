from fastapi import APIRouter
from .usuarios.models import Usuario
from .usuarios.routes import router as router_usuarios

Usuario.model_rebuild()

router = APIRouter()

router.include_router(router_usuarios, prefix="/usuarios")  