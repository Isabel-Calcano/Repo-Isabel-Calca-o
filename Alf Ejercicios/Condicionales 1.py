# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = input("Por favor indique su edad en años: ")
edad = edad.replace(" ", "")

if edad.isnumeric():
    edad = int(edad)

    if edad >= 18:
        print(f"Usted es mayor de edad, teniendo {edad}")
    else:
        print(f"Useted es menor de edad, teniendo {edad}")

else:
    print("Ha ocurrido un error, por favor intente de nuevo")

