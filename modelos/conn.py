import psycopg2
import os

def obtener_conexion():
    try:
        conn = psycopg2.connect(
            os.environ.get("DATABASE_URL"),
            sslmode="require"
        )
        return conn
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        raise