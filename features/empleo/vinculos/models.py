from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime

class Vinculo(SQLModel, table=True):
    __tablename__ = "tbVinculoLaboral"
    __table_args__ = {"schema": "Empleo"}
    
    vinculo: str | None = Field(default=None, primary_key=True)
    codigo: str
    dni: str
    categoria: str
    regimen_laboral: str = Field(sa_column=Column("regimenlaboral", String))
    remuneracion: float
    area: str
    documento: str
    puesto_empleo: str = Field(sa_column=Column("puestoempleo", String))
    tipo_empleado: str = Field(sa_column=Column("tipoempleado", String))
    fecha_inicio: datetime = Field(sa_column=Column("fechainicio", DateTime))
    fechafin: datetime = Field(sa_column=Column("fechafin", DateTime))
    tipo_vinculo: str = Field(sa_column=Column("tipovinculo", String))
    periodo: str
    nuevo_vinculo: bool = Field(sa_column=Column("nuevovinculo", Boolean))
    fecha: datetime
    fecha_modificacion: datetime = Field(sa_column=Column("fechamodificacion", DateTime))
    proceso_ingreso: str = Field(sa_column=Column("procesoingreso", String))
    condicion: str
    usuario: str
    usuario_modificacion: str = Field(sa_column=Column("usuariomodificacion", String))
    
    estado: bool
    observacion: str

    # -------------------------------- RELACIONES Y CLAVES FORANEAS --------------------------------
    dependencia: Optional[str] = Field(default=None, foreign_key="General.tbDependencia.dependencia")
    dependencia_rel: List["Dependencia"] = Relationship(back_populates="vinculos_rel") # type: ignore
    
    funcion: Optional[str] = Field(default=None, foreign_key="Empleo.tbFuncion.funcion")
    funcion_rel: List["Funcion"] = Relationship(back_populates="vinculos_rel") # type: ignore
    
    dni: str = Field(default=None, foreign_key="General.tbPersona.dni")
    dni_rel: List["Persona"] = Relationship(back_populates="vinculos_rel") # type: ignore
    



