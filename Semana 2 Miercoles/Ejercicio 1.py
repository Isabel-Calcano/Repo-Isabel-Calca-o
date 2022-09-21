# Ver  si el numero introducido es primo o no.
number = int(input("please enter a number: "))
aux = number - 1
cont = 0

while aux > 1:
    if number == 0:
        cont += 1
        break
        # se puede poner break o continue para afectar el while.
    aux -= 1

if cont == 0:
    print(f"The number {number} is prime")

print("hola")