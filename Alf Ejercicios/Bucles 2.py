# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = input("Indica tu edad \n--> ")
edad = int(edad)

count = 0
while count < edad:
    count += 1
    print(f"Llegaste a tener {count} años de edad")