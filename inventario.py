
# Este programa solicita al usuario el nombre, precio y cantidad de un producto.

nombre = input("Ingrese el nombre del producto: ")

while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("Error: el precio no puede ser negativo.")
        else:
            break
    except ValueError:
        print("Error: debe ingresar un número válido para el precio.")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad < 0:
            print("Error: la cantidad no puede ser negativa.")
        else:
            break
    except ValueError:
        print("Error: debe ingresar un número entero válido para la cantidad.")

costo_total = precio * cantidad

print("\n-- Resultado --")
print("Producto:", nombre)
print("Precio unitario:", precio)
print("Cantidad:", cantidad)
print("Costo total:", costo_total)

print(f"\nProducto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

"""Este programa permite registrar un producto en un inventario solicitando
su nombre, precio y cantidad. Valida que precio y cantidad sean números
correctos, calcula el costo total multiplicando el precio por la cantidad
y finalmente muestra toda la información en pantalla."""

