from fastapi import APIRouter
from .vinculos.models import Vinculo
from .vinculos.routes import router as router_vinculos
from .movimientos.routes import router as router_movimientos

Vinculo.model_rebuild()

router = APIRouter()

router.include_router(router_vinculos, prefix="/vinculos")
router.include_router(router_movimientos, prefix="/movimientos")


