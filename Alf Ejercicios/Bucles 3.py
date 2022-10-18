# Escribir un programa que pida al usuario un número entero positivo y muestre por 
# pantalla todos los números impares desde 1 hasta ese número separados por comas.

num = input("Escriba un numero entero positivo \n--> ")

if num.isnumeric():
    num = int(num)
    count = 0

    while count <= num:

        if count % 2 == 0:
            pass

        else:
            print(f"El numero {count} es impar")

        count += 1

else:
    print("Ha ocurrido un error, por favor intente de nuevo")

# OTRA FORMA 

num = input("Escriba un numero entero positivo \n--> ")

if num.isnumeric():
    num = int(num)
else:
    print("Ha ocurrido un error, por favor intente de nuevo")

for i in range(1, num+1, 2):
    print(i, end= ", ")