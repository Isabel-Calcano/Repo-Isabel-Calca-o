# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña = input("Cree una contraseña: ")
intento = 1

while contraseña != intento:
    intento = input("Cual es su contraseña? \n--> ")

print("***Contraseña correcta***")