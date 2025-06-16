from sqlmodel import SQLModel, Field

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name : str

import pyodbc

# Configuración de la conexión
server = '10.0.0.121'
database = 'rh'
username = 'bperez' 
password = '72519692' 

