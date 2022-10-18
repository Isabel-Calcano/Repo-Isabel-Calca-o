# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
# la cuenta atrás desde ese número hasta cero separados por comas.

num = input("Escriba un numero entero positivo \n--> ")

if num.isnumeric():
    num = int(num)
else:
    print("Ha ocurrido un error, por favor intente de nuevo")

for i in range(num, -1, -1):
    print(i, end= ", ")