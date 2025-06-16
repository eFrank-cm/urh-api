from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String

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
    usuario: str
    estado: bool
    fecha: str
    fechadefuncion: str
    ubigeonac: str