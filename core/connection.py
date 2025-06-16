from sqlmodel import create_engine, Session
from sqlalchemy.engine import URL
from .config import settings

# Crear URL de conexión
connection_url = URL.create(
    "mssql+pyodbc",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    database=settings.DB_NAME,
    query={"driver": settings.DB_DRIVER}
)

# Crear engine global reutilizable
engine = create_engine(connection_url, echo=False)

def get_session():
     with Session(engine) as session:
         yield session
