# Escribir un programa que pida al usuario dos números enteros y muestre por 
# pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> 
# son los números introducidos por el usuario, y <c> y <r> son el cociente y 
# el resto de la división entera respectivamente.

n = input("Escribe un numero: ")
m = input("Escribe otro numero: ")

c = float(n) / float(m)
c = int(c)
r = float(n) % float(m)
r = int(r)
print(f"al dividir {n} entre {m}, da un cociente de {c} y un resto de {r}")