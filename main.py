from typing import Union
from contextlib import asynccontextmanager
from sqlalchemy import text
from app.system.db import Base, engine, wait_for_db
from app.modules.auth.routes import router as auth_router
from fastapi import FastAPI

# Lifespan para manejar startup seguro
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1️⃣ Esperar a que la DB esté lista
    wait_for_db(engine)

    # 2️⃣ Crear esquemas si no existen
    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS auth"))
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS core"))

    # 3️⃣ Crear tablas
    Base.metadata.create_all(bind=engine)

    yield  # aquí empieza la app

app = FastAPI(lifespan=lifespan)

# Registrar routers
app.include_router(auth_router)