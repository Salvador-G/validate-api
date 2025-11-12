import time
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:password@db:5432/app_db")

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"connect_timeout": 10}  # espera 10 segundos
)

# Crear los esquemas si no existen
with engine.begin() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS auth"))
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS core"))
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Función para esperar a que la DB esté lista
def wait_for_db(engine, retries=10, delay=2):
    for i in range(retries):
        try:
            with engine.connect():
                print("Conexión a la DB establecida")
                return
        except OperationalError:
            print(f"DB no lista, reintentando ({i+1}/{retries})...")
            time.sleep(delay)
    raise RuntimeError("No se pudo conectar a la DB después de varios intentos")

# Dependency para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()