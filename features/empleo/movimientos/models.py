from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime

class Movimiento(SQLModel, table=True):
    __tablename__ = "tbMovimiento"
    __table_args__ = {"schema": "Empleo"}
    
    movimiento: int = Field(primary_key=True)
    tipo_movimiento: str | None = Field(sa_column=Column("tipomovimiento", String))
    dni: str
    documento: str | None
    fecha_inicio: datetime = Field(sa_column=Column("fechainicio", DateTime))
    fecha_fin: datetime | None = Field(default=None, sa_column=Column("fechafin", DateTime))
    estado: str | None
    observacion: str | None
    descripcion: str | None
    nro_expediente: str | None = Field(sa_column=Column("nroexpediente", String))
    
    # -------------------------------- RELACIONES Y CLAVES FORANEAS --------------------------------
    dependencia: str = Field(foreign_key="General.tbDependencia.dependencia")
    dependencia_rel: "Dependencia" = Relationship(back_populates="movimientos_rel")  # type: ignore
    
    funcion: str | None = Field(foreign_key="Empleo.tbFuncion.funcion")
    funcion_rel: "Funcion" = Relationship(back_populates="movimientos_rel") # type: ignore
    
    vinculo: str | None = Field(foreign_key="Empleo.tbVinculoLaboral.vinculo")
    vinculo_rel: "Vinculo" = Relationship(back_populates="movimientos_rel") # type: ignore