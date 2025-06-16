import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Settings:
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_DRIVER: str = os.getenv("DB_DRIVER")

settings = Settings()
