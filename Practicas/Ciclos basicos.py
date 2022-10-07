nombre = " "

while nombre == " " or nombre.isspace():
    print('El nombre no se puede quedar en blanco')
    nombre= input('Por favor escribe un nombre: ')

print(nombre)