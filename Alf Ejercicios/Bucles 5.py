# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número 
# de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

cantidad = float(input("Indique la cantidad a invertir: "))
años = int(input("Indique el numero de años: "))
interes = float(input("Indique el interes anual: "))


for i in range(años):
    cantidad *= (1 + interes / 100)
    print("En el año", i+1," se recibirá", round(cantidad, 2))




