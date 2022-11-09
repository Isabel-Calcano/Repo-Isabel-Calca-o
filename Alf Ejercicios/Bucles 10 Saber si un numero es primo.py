# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

num = input("Escriba un numero entero: ")

if num.isnumeric():
    num = int(num)
    aux = 2
    while num % aux != 0 :
        aux += 1

    if aux != num:
        print(f"El numero {num} NO es primo")
    else:
        print(f"El numero {num} es primo")
else:
    print("No ha introducido los datos correctamente, por favor intente de nuevo.")