from fastapi import APIRouter
from intranet.usuario.models import Usuario
from intranet.usuario.routes import router as router_usuarios

Usuario.model_rebuild()

router = APIRouter()

router.include_router(router_usuarios, tags=["Usuarios"])