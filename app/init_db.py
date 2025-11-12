from app.system.db import Base, engine
from app.modules.auth import models as auth_models
from app.system import models as core_models

print("🔧 Creando tablas en PostgreSQL...")
Base.metadata.create_all(bind=engine)
print("✅ Listo.")
