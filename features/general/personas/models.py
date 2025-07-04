from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String
from typing import List
from datetime import datetime

class Persona(SQLModel, table=True):
    __tablename__ = "tbPersona"
    __table_args__ = {"schema": "General"}

    dni: str | None = Field(default=None, primary_key=True)
    nombres: str = Field(sa_column=Column("nombre", String))
    direccion: str
    telefono: str
    celular: str
    email: str
    correo_institucional: str = Field(sa_column=Column("correoinstitucional", String))
    fecha_nacimiento: str = Field(sa_column=Column("fechanacimiento", String))
    genero: str
    imagen: str
    
    # datos complementarios
    ubigeo: str
    tipodocumentoidentidad: str
    estado: bool
    fecha: datetime
    fechadefuncion: str
    ubigeonac: str
    usuario: str
    
    # -------------------------------- RELACIONES Y CLAVES FORANEAS --------------------------------
    vinculos_rel: List["Vinculo"] = Relationship(back_populates="dni_rel") # type: ignore
    
    usuarios_rel: List["Usuario"] = Relationship(back_populates="persona_rel") # type: ignore
    
    