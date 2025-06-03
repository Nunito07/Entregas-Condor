from modelos import clientes

def mostrar_menu():
    print("\n=== MENÚ DE CLIENTES ===")
    print("1. Insertar cliente")
    print("2. Ver todos los clientes")
    print("3. Buscar cliente por ID")
    print("4. Actualizar cliente")
    print("5. Eliminar cliente")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            email = input("Email del cliente: ")
            clientes.insertar_cliente(nombre, email)

        elif opcion == "2":
            lista = clientes.obtener_todos_los_clientes()
            for c in lista:
                print(f"ID: {c[0]}, Nombre: {c[1]}, Email: {c[2]}")

        elif opcion == "3":
            cliente_id = input("ID del cliente: ")
            cliente = clientes.obtener_cliente_por_id(cliente_id)
            if cliente:
                print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Email: {cliente[2]}")
            else:
                print("Cliente no encontrado.")

        elif opcion == "4":
            cliente_id = input("ID del cliente a actualizar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_email = input("Nuevo email: ")
            clientes.actualizar_cliente(cliente_id, nuevo_nombre, nuevo_email)

        elif opcion == "5":
            cliente_id = input("ID del cliente a eliminar: ")
            clientes.eliminar_cliente(cliente_id)

        elif opcion == "0":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
