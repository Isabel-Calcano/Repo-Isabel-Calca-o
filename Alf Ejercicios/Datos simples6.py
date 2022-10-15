while True:

    n= input("Escribe un numero entero: \n-->")

    if n.isnumeric():
        n = int(n)
        r = n * ( n + 1 ) / 2
        r = int(r)
        print(f"La suma de los {n} primeros enteros positivos resulta en {r} \n")
    else:
        print(f"Ha ocurrido un error con '{n}', por favor intente de nuevo")
    
