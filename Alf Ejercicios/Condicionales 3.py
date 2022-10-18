# Escribir un programa que pida al usuario dos números y muestre por pantalla 
# su división. Si el divisor es cero el programa debe mostrar un error.

num_1 = input("Escribe un numero: ")
num_2 = input("Escribe otro numero: ")

if num_2 == "0":
    print("Error, no se puede dividir entre 0")
else:
    print(round(float(num_1) / float(num_2) , 2))