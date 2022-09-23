comprar= input("""***Bienvenidos a mi tienda de zapatos***
¿Desea comprar algo?
(S/s => si) (N/n) => no)
            
==> """)

while(True):
    if comprar.upper() == "S":
       zapatos = input("""¿Que zapatos quieres?
        Tacones
        Deportivos
        Sandalias
        Alpargatas
        ==> """)
        if zapatos.upper() == TACONES:
            pass
        elif zapatos.upper() == DEPORTIVOS:
            pass
        elif zapatos.upper() == SANDALIAS:
            pass
        elif zapatos.upper() == ALPARGATAS:
            pass
        break

    elif comprar.upper() == "N":
        print("Adios")

    else:
        print("""Error al introducir los datos, por favor ingreselo de nuevo.""")
        break