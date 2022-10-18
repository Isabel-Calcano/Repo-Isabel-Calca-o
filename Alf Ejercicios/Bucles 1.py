# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra = input("Escriba una palabra: ")
print(f"{palabra}\n" * 10)
print("***\n")

# otro método:

# palabra = input("Escriba una palabra: ")
for i in range(10):
    print(palabra)