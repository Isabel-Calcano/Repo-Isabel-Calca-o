num= input("Escribe un numero entero positivo: ")
aux= 1

if num.isnumeric():
    num= int(num)
    while aux < num:
        if aux + 2 < num:
            print(aux)
        print(aux,end=",")
        aux+=2

else:
     print("input error")    