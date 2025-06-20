from fastapi import FastAPI
from features.general import router as router_general
from features.empleo import router as router_empleo
from features.intranet import router as router_intranet
from core.cors import add_cors_middleware

app = FastAPI()

add_cors_middleware(app)

app.include_router(router_general, prefix="/general", tags=["General"])
app.include_router(router_empleo, prefix="/empleo", tags=["Empleo"])
app.include_router(router_intranet, prefix="/intranet", tags=["Intranet"])
