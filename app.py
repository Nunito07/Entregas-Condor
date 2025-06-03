from flask import Flask, render_template, request, redirect, url_for
from modelos import clientes  # Ajusta según tu estructura de carpetas

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/clientes", methods=["GET", "POST"])
def clientes_lista():
    if request.method == "POST":
        accion = request.form.get("accion")
        
        if accion == "insertar":
            nombre = request.form.get("nombre")
            email = request.form.get("email")
            clientes.insertar_cliente(nombre, email)
        
        elif accion == "actualizar":
            cliente_id = request.form.get("cliente_id")
            nuevo_nombre = request.form.get("nombre")
            nuevo_email = request.form.get("email")
            clientes.actualizar_cliente(cliente_id, nuevo_nombre, nuevo_email)
        
        elif accion == "eliminar":
            cliente_id = request.form.get("cliente_id")
            clientes.eliminar_cliente(cliente_id)
        
        return redirect(url_for("clientes_lista"))

    # GET: mostrar lista
    lista_clientes = clientes.obtener_todos_los_clientes()
    return render_template("clientes.html", clientes=lista_clientes)

@app.route("/productos")
def productos():
    return render_template("productos.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

