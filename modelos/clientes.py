from .conn import obtener_conexion

# Crear (ya lo tienes)
def insertar_cliente(nombre, email):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        sql = "INSERT INTO clientes (nombre, email) VALUES (%s, %s)"
        cursor.execute(sql, (nombre, email))
        conn.commit()
        print("Cliente insertado correctamente.")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error al insertar cliente:", e)

# Leer todos
def obtener_todos_los_clientes():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        sql = "SELECT id, nombre, email FROM clientes"
        cursor.execute(sql)
        clientes = cursor.fetchall()
        cursor.close()
        conn.close()
        return clientes
    except Exception as e:
        print("Error al obtener clientes:", e)
        return []

# Leer por ID
def obtener_cliente_por_id(cliente_id):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        sql = "SELECT id, nombre, email FROM clientes WHERE id = %s"
        cursor.execute(sql, (cliente_id,))
        cliente = cursor.fetchone()
        cursor.close()
        conn.close()
        return cliente
    except Exception as e:
        print("Error al buscar cliente:", e)
        return None

# Actualizar
def actualizar_cliente(cliente_id, nuevo_nombre, nuevo_email):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        sql = "UPDATE clientes SET nombre = %s, email = %s WHERE id = %s"
        cursor.execute(sql, (nuevo_nombre, nuevo_email, cliente_id))
        conn.commit()
        print("Cliente actualizado correctamente.")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error al actualizar cliente:", e)

# Eliminar
def eliminar_cliente(cliente_id):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        sql = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(sql, (cliente_id,))
        conn.commit()
        print("Cliente eliminado correctamente.")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error al eliminar cliente:", e)
