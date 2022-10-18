# Escribir un programa que pregunte por consola por los productos de una 
# cesta de la compra, separados por comas, y muestre por pantalla cada uno 
# de los productos en una línea distinta.

productos = input("Indique los productos de la cesta de compras, separados por comas: ")
productos = productos.replace(" ", "")
productos = productos.replace(",", "\n")
print(productos)