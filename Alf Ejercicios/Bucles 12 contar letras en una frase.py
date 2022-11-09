# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Escriba una frase: ")
letra = input("Escriba una letra: ")
aux = 0

for i in frase:
    if i == letra:
        aux += 1
    else:
        pass

# OR cuenta = frase.count(letra)
print(f'En la frase "{frase}" hay {aux} veces la letra "{letra}"')

