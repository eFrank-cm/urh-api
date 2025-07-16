from pydantic import BaseModel, ConfigDict
from .models import Vinculo
from datetime import datetime
from features.utils import to_camel
    
class VinculoRequest(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    
    # DATOS DEL EMPLEADO
    nro_documento: str
    apellido_paterno: str
    apellido_materno: str
    nombres: str
    genero: str | None
    fecha_nacimiento: datetime | None
    celular: str
    correo_institucional: str   | None
    
    # DATOS DEL VINCULO
    vinculo: str
    tipo_vinculo: str
    tipo_empleado: str
    regimen_laboral: str
    categoria: str
    funcion: str
    documento: str
    dependencia_documento: str
    fecha_inicio: datetime
    fecha_fin: datetime | None

def ds_vinculo_request(vinculo: Vinculo) -> VinculoRequest:
    partes = [p.strip() for p in vinculo.dni_rel.nombres.split("-")]
    
    return VinculoRequest(
        nro_documento = vinculo.dni,    
        apellido_paterno = partes[0] if len(partes) > 0 else "",
        apellido_materno = partes[1] if len(partes) > 1 else "",
        nombres = partes[2] if len(partes) > 2 else "",
        genero = vinculo.dni_rel.genero,
        fecha_nacimiento = vinculo.dni_rel.fecha_nacimiento,
        celular = vinculo.dni_rel.telefono,
        correo_institucional = vinculo.dni_rel.correo_institucional,

        vinculo = str(vinculo.vinculo),
        tipo_vinculo = vinculo.tipo_vinculo,
        tipo_empleado = TIPO_EMPLEADO[vinculo.tipo_empleado],
        regimen_laboral = vinculo.regimen_laboral,
        categoria = vinculo.categoria,
        funcion = vinculo.funcion_rel.descripcion if vinculo.funcion_rel else None,
        documento=vinculo.documento,
        dependencia_documento = vinculo.dependencia_rel.descripcion if vinculo.dependencia_rel else None,
        fecha_inicio = vinculo.fecha_inicio,
        fecha_fin = vinculo.fecha_fin
    )

TIPO_EMPLEADO = {
    "A": "ADMINISTRATIVO",
    "D": "DOCENTE",
    "AP": "APOYO DOCENTE",
    "PRA": "PRACTICAS",
}