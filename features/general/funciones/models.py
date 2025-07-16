from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String
from typing import List

class Funcion(SQLModel, table=True):
    __tablename__ = "tbFuncion"
    __table_args__ = {"schema": "Empleo"}
    
    funcion : int | None = Field(default=None, primary_key=True)
    descripcion: str
    categoria: str
    abreviacion: str
    estado: bool
    tipo: str = Field(sa_column=Column("_tipo", String))
    
    # -------------------------------- RELACIONES Y CLAVES FORANEAS --------------------------------
    vinculos_rel: List["Vinculo"] = Relationship(back_populates="funcion_rel") # type: ignore
    movimientos_rel: List["Movimiento"] = Relationship(back_populates="funcion_rel") #type: ignore
    
