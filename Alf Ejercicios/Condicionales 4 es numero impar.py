# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

n = input("por favor escriba un numero: ")

if n.isnumeric():
    m = float(n)
    m = m % 2
    if m == 0:
        print(f"El numero {n} es par")
    else:
        print(f"el numero {n} es impar")
else:
    print("Se debe introducir un numero, por favor intente de nuevo")