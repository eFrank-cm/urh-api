from fastapi import FastAPI
from general import router as router_general
from empleo import router as router_empleo
from intranet import router as router_intranet

app = FastAPI()

app.include_router(router_general, prefix="/general", tags=["General"])
app.include_router(router_empleo, prefix="/empleo", tags=["Empleo"])
app.include_router(router_intranet, prefix="/intranet", tags=["Intranet"])
