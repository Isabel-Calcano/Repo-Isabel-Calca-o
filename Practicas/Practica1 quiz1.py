#Indicar si un numero es repunit y cuadrado
numero= input("Please write a number: ")

if numero.isnumeric():
    str(numero)
    cantidad_digitos= len(numero)
    contador= 1
    while contador <= cantidad_digitos:
        for d in numero:
            repeticion_de_digitos= numero.count(d)
            contador += 1
            if repeticion_de_digitos == cantidad_digitos:
                print("El numero {} es repunit".format(numero))
            else:
                print("El numero {} no es repunit".format)

else:
    print("Input Error, please try again")






    #numero_copy= numero
    #numero= list(numero)
    #print(numero)
    #numero_copy= list(numero_copy)
    #print(numero_copy)