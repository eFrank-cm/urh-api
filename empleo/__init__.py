from fastapi import APIRouter
from empleo.vinculos.models import Vinculo
from empleo.vinculos.routes import router as router_vinculos

Vinculo.model_rebuild()


router = APIRouter()

router.include_router(router_vinculos)


