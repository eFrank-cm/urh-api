from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime

class Usuario(SQLModel, table=True):
    __tablename__ = "tbUsuario"
    __table_args__ = {"schema": "Intranet"}
    
    password: str = Field(sa_column=Column("passw", String))
    last_session: datetime = Field(sa_column=Column("ultfechaacceso", DateTime))
    create_at: datetime = Field(sa_column=Column("fecha", DateTime))
    clave_temporal: str = Field(sa_column=Column("clavetemporal", String))
    vigencia: datetime
    correo_reseteo: str = Field(sa_column=Column("correoreseteo", String))
    estado: bool
    
    # -------------------------------- RELACIONES Y CLAVES FORANEAS --------------------------------
    dni: Optional[str] = Field(default=None, foreign_key="General.tbPersona.dni",  primary_key=True)
    persona_rel: Optional["Persona"] = Relationship(back_populates="usuarios_rel") # type: ignore
    



