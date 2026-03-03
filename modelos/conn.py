import psycopg2
import os

def obtener_conexion():
    try:
        print("DATABASE_URL usada:", os.environ.get("DATABASE_URL"))
        conn = psycopg2.connect(
            os.environ.get("DATABASE_URL"),
            sslmode="require"
        )
        print("Conexión establecida correctamente")
        return conn
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        raise