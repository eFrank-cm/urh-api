from fastapi import APIRouter
from .vinculos.models import Vinculo
from .vinculos.routes import router as router_vinculos

Vinculo.model_rebuild()

router = APIRouter()

router.include_router(router_vinculos, prefix="/vinculos")


