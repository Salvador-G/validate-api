from logging.config import fileConfig
import sys
import os
from dotenv import load_dotenv

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Agregar la raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de Alembic
config = context.config


# Reemplaza la URL del alembic.ini por la de tu .env
database_url = os.getenv("DATABASE_URL")
if database_url is None:
    raise ValueError("No se encontró DATABASE_URL en el .env")
config.set_main_option("sqlalchemy.url", database_url)

# Configuración de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# Importar metadata de todos los modelos
from app.modules.base import all_metadata
target_metadata = all_metadata

# Función para migraciones offline
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        include_schemas=True,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Función para migraciones online
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            include_schemas=True,
            compare_type=True,
            compare_server_default=True
            )

        with context.begin_transaction():
            context.run_migrations()

# Ejecuta según el modo
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
