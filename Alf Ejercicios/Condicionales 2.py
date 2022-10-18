# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseña = input("Cree una contraseña: ")
contraseña = contraseña.upper()

contraseña_nueva = input("Escriba su contraseña: ")
contraseña_nueva = contraseña_nueva.upper

if contraseña == contraseña_nueva:
    print("Contraseña correcta, bienvendio.")
    
else:
    print("Contraseña incorrecta, por favor intente de nuevo.")