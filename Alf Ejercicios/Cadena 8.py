# Escribir un programa que pregunte por consola el precio de un producto 
# en euros con dos decimales y muestre por pantalla el número de euros y 
# el número de céntimos del precio introducido.

precio = input("Indique el precio del producto con dos decimales: ")
precio = round(float(precio) , 2)
precio = str(precio)

print(precio[0:precio.find(".")] , "euros con " , precio[-2:], "céntimos")
