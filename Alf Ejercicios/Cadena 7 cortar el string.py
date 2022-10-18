# Escribir un programa que pregunte el correo electrónico del usuario en la consola 
# y muestre por pantalla otro correo electrónico con el mismo nombre 
# (la parte delante de la arroba @) pero con dominio ceu.es.

correo = input("Escriba su correo:\n--> ")
if "@" in correo:
    posicion = correo.index("@")
    nuevo_correo = correo[:posicion]
    print(nuevo_correo + "@ceu.es")
else:
    print("ha ocurrido un herror, por favor intente de nuevo")
