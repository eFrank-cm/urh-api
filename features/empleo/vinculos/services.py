from sqlmodel import Session, select
from .models import Vinculo

# encontra vinculos activos
def search_vinculos_activos(session: Session):
    docentes_nombrados = session.exec(
        select(Vinculo).where(
            (Vinculo.tipo_vinculo == "NOM") & (Vinculo.tipo_empleado == "D") & (Vinculo.estado == "A")
        )
    ).all()
    
    vistos = set()
    unicos = []
    
    for v in docentes_nombrados:
        if v.dni not in vistos:
            vistos.add(v.dni)
            unicos.append(v)
    
    vinculos = unicos   
    return vinculos
    