# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y 
# muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 
# dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 
# dígitos enteros y 2 decimales.

nombre = input("Escriba el nombre del producto: ")
precio = input("Escriba el precio del producto con dos decimales: ")
cantidad = input("Escriba la cantidad de unidades de producto: ")

precio = round(float(precio) , 2)
precio = str(precio)
length_precio = len(precio)
precio = ("0" * (9 - length_precio)) + precio

length_cantidad = len(cantidad)
cantidad = ("0" * (3 - length_cantidad)) + cantidad

total = round(float(precio) * int(cantidad), 2)

print(f"*** Factura ***\nProducto: {nombre} \nPrecio x unidad: {precio} \nN° Unidades: {cantidad} \nTotal: {total}")
