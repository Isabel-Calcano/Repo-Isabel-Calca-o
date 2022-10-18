# Para tributar un determinado impuesto se debe ser mayor de 16 años y 
# tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir 
# un programa que pregunte al usuario su edad y sus ingresos mensuales 
# y muestre por pantalla si el usuario tiene que tributar o no.

edad = input("Indica tu edad \n--> ")
ingresos = input("Indica tus ingresos en € \n--> ")

edad = edad.replace(" ", "")
ingresos = ingresos.replace(" ", "")
ingresos = ingresos.replace("€", "")

if edad.isnumeric() and ingresos.isnumeric():
    edad = int(edad)
    ingresos = float(ingresos)
    if edad > 16 and ingresos >= 1000:
        print("Si debe tributar")
    else:
        print("No debe tributar")
else:
        print("Ha ocurrido un error, por favor ingrese los datos de nuevo")