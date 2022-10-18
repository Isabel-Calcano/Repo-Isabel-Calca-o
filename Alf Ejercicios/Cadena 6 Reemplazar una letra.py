# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
# y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = input("Escriba una palabra o frase: ")
letra = input("Escriba una letra: ")
letra_mayus = letra.upper()

frase = frase.replace(letra, letra_mayus)
print(frase)