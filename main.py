from typing import Union
from app.system.db import Base, engine
from app.modules.auth.routes import router as auth_router
from fastapi import FastAPI

# Crear las tablas si no existen (solo para pruebas iniciales)
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Registrar los routers
app.include_router(auth_router)