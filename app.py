from flask import Flask, render_template, request, redirect, url_for
from modelos import clientes  # Ajusta según tu estructura de carpetas

app = Flask(__name__)

@app.route("/clientes", methods=["GET", "POST"])
def clientes_lista():
    print("🔵 Entró a la ruta /clientes")

    if request.method == "POST":
        accion = request.form.get("accion")
        print("📌 Acción recibida:", accion)

        if accion == "insertar":
            nombre = request.form.get("nombre")
            email = request.form.get("email")
            print("➕ Insertando:", nombre, email)
            clientes.insertar_cliente(nombre, email)

        elif accion == "actualizar":
            cliente_id = request.form.get("cliente_id")
            nuevo_nombre = request.form.get("nombre")
            nuevo_email = request.form.get("email")
            print("✏️ Actualizando:", cliente_id, nuevo_nombre, nuevo_email)
            clientes.actualizar_cliente(cliente_id, nuevo_nombre, nuevo_email)

        elif accion == "eliminar":
            cliente_id = request.form.get("cliente_id")
            print("🗑️ Eliminando:", cliente_id)
            clientes.eliminar_cliente(cliente_id)

        return redirect(url_for("clientes_lista"))

    # GET: mostrar lista
    print("📥 Ejecutando obtener_todos_los_clientes()...")
    lista_clientes = clientes.obtener_todos_los_clientes()

    print("📋 Clientes encontrados:", lista_clientes)
    print("🔢 Total clientes:", len(lista_clientes))

    return render_template("clientes.html", clientes=lista_clientes)