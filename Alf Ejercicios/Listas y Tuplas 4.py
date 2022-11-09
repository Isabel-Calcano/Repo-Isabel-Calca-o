# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

numeros = []

for i in range(6):
    n = int(input("escriba los numeros de la loteria: "))
    numeros.append(n)
numeros.sort()

print("Los numeros ganadores son: ", numeros)