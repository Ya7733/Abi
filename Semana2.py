# Lista global para almacenar los productos
inventario = []


def agregar_producto():
    """Solicita datos al usuario y añade un producto al inventario."""
    try:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            return

        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))

        if precio < 0 or cantidad < 0:
            print("Error: El precio y la cantidad deben ser valores positivos.")
            return

        # TASK 2: Crear el diccionario y añadirlo a la lista
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        inventario.append(producto)
        print(f"✅ Producto '{nombre}' agregado exitosamente.")
    except ValueError:
        print("❌ Error: Ingrese valores numéricos válidos para precio y cantidad.")


def mostrar_inventario():
    """TASK 3: Recorre y muestra todos los productos registrados."""
    if not inventario:
        print("\n⚠️ El inventario está vacío.")
    else:
        print("\n--- INVENTARIO ACTUAL ---")
        for p in inventario:
            # Formato claro: Producto | Precio | Cantidad
            print(
                f"Producto: {p['nombre']} | Precio: ${p['precio']:.2f} | Cantidad: {p['cantidad']}"
            )


def calcular_estadisticas():
    """TASK 4: Calcula el valor total y la cantidad de productos."""
    if not inventario:
        print("\n⚠️ No hay datos para calcular estadísticas.")
        return

    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    total_items = sum(p["cantidad"] for p in inventario)
    total_registros = len(inventario)

    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
    print(f"💰 Valor total del inventario: ${valor_total:.2f}")
    print(f"📦 Cantidad total de unidades: {total_items}")
    print(f"📝 Total de productos distintos: {total_registros}")


def menu():
    """TASK 1 & 2: Menú interactivo dentro de un bucle while."""
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        # TASK 1: Validación de opciones con condicionales
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")


# Ejecución del programa
if __name__ == "__main__":
    menu()

# TASK 5: Resumen del objetivo de la semana
# El objetivo de esta semana ha sido consolidar el uso de estructuras fundamentales:
# control de flujo (bucles y condicionales), manejo de colecciones (listas y diccionarios)
# y la organización del código mediante funciones para crear aplicaciones interactivas.
