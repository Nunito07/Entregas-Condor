import psycopg2

def obtener_conexion():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="entregascondor_bd",
            user="juanzuluaga",
            password=""
        )
        return conn
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        raise  # vuelve a lanzar el error para que quien llame lo maneje
