from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String
from typing import List

class Dependencia(SQLModel, table=True):
    __tablename__ = "tbDependencia"
    __table_args__ = {"schema": "General"}
    
    dependencia: str | None = Field(default=None, primary_key=True)
    rof: str
    descripcion: str
    dependencia_padre: str = Field(sa_column=Column("dependenciapadre", String))
    tipo_dependencia: str = Field(sa_column=Column("tipodependencia", String))
    id: str
    codigo: str
    nivel: str
    abreviacion: str
    categoria_dependencia: str = Field(sa_column=Column("categoriadependencia", String))
    gestion: str
    descripcion_tipo: str = Field(sa_column=Column("descripciontipo", String))
    local: str
    codlocal: str
    
    observacion: str
    estado: bool
    
    # -------------------------------------------------------------------------------
    vinculos_rel: List["Vinculo"] = Relationship(back_populates="dependencia_rel") # type: ignore