# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
# el número de años, y muestre por pantalla el capital obtenido en la inversión.


inversion = input("Escribe la cantidad a invertir: $")
inversion = float(inversion)

interes = input("Cual es la taza de interes porcentual anual: ")
interes = float(interes)


años = input("Cantidad de años a inveritr: ")
años = float(años)

obtenido = round(inversion * (interes / 100 + 1) ** años, 2)
print(f"Con la inversion incicial se ha obtenido ${obtenido}")