num= input("Escribe un numero entero positivo: ")

if num.isnumeric():
    num= int(num)
    num= num + 1
    for index in range(0,num):
        print("*"* index)

else:
     print("input error")    

