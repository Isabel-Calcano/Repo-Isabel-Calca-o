# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un 
# nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al 
# usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Escriba su nombre: ")
sexo = input("¿Es mujer o hombre? indique con 'm' o 'h'\n--> ")

nombre = nombre.lower()

letras_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
letras_b = ['ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if (nombre[0] in letras_a and sexo == "m") or (nombre[0] in letras_b and sexo == "h"):
    print("Estas en el equipo A")
else:
    print("Estas en el equipo B")

