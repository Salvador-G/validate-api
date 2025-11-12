from system.db import engine
from sqlalchemy import text

def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            print("✅ Conexión exitosa a la base de datos")
            for row in result:
                print(f"Versión de PostgreSQL: {row[0]}")
    except Exception as e:
        print("❌ Error al conectar a la base de datos:")
        print(e)

if __name__ == "__main__":
    test_connection()
