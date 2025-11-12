from typing import Union
from app.system.db import Base, engine
from app.modules.auth.routes import router as auth_router
from fastapi import FastAPI

app = FastAPI()
# Crear tablas al iniciar la aplicación
@app.on_event("startup")
def startup_event():
    print("🔹 Creando tablas si no existen...")
    Base.metadata.create_all(bind=engine)

# Registrar routers
app.include_router(auth_router)