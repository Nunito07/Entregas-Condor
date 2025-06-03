from .conn import conectar

def insertar_producto(nombre, precio, stock):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, precio, stock))
        conn.commit()
        print("Producto insertado correctamente.")
    except Exception as e:
        print("Error al insertar producto:", e)
    finally:
        conn.close()

def obtener_todos_los_productos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        return cursor.fetchall()
    except Exception as e:
        print("Error al obtener productos:", e)
        return []
    finally:
        conn.close()

def obtener_producto_por_id(producto_id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = %s", (producto_id,))
        return cursor.fetchone()
    except Exception as e:
        print("Error al buscar producto:", e)
        return None
    finally:
        conn.close()

def actualizar_producto(producto_id, nuevo_nombre, nuevo_precio, nuevo_stock):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "UPDATE productos SET nombre = %s, precio = %s, stock = %s WHERE id = %s"
        cursor.execute(sql, (nuevo_nombre, nuevo_precio, nuevo_stock, producto_id))
        conn.commit()
        print("Producto actualizado correctamente.")
    except Exception as e:
        print("Error al actualizar producto:", e)
    finally:
        conn.close()

def eliminar_producto(producto_id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = %s", (producto_id,))
        conn.commit()
        print("Producto eliminado correctamente.")
    except Exception as e:
        print("Error al eliminar producto:", e)
    finally:
        conn.close()
