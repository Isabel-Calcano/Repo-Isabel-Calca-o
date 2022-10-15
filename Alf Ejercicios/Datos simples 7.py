# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, 
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
# es el índice de masa corporal calculado redondeado con dos decimales.

peso = input("Por favor indique su peso en Kg: ")
peso = float(peso)
print(f"Su peso es de {peso} Kg.")

estatura = input("Por favor indique su estatura en metros: ")
estatura = float(estatura)
print(f"Tu estatura es de {estatura} m.")

imc = round(peso / estatura ** 2 , 2)
print(f"Su indice de masa corporal 'IMC' es de: {imc} kg/m")
