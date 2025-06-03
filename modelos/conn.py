import psycopg2

def obtener_conexion():
    try:
        conn = psycopg2.connect(
            host="postgresql://root:CfaSAYkRnGA56sW5YLV4xfAhAuNS3dGh@dpg-d0v66cvfte5s739a9j7g-a.oregon-postgres.render.com/entregascondor_bd",
            database="entregascondor_bd",
            user="root",
            password="CfaSAYkRnGA56sW5YLV4xfAhAuNS3dGh"
        )
        return conn
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        raise  # vuelve a lanzar el error para que quien llame lo maneje
