puntuacion = input("Indique si el empleado tiene una puntuacion de '0.0', '0.4' o '0.6': ")
bono = 2400

if puntuacion == "0.0":
    nivel = "inaceptable"
elif puntuacion == "0.4":
    nivel = "aceptable"
elif puntuacion == "0.6":
    nivel = "Meritorio"
else:
    nivel = "No existe"

if nivel == "No existe":
    print("No se introdujo los datos correctamente, intente de nuevo")
else:
    print(f"Como el empleado es del nivel de rendimiento {nivel}, recibirá un bono de", (round((float(puntuacion) * bono), 2)))