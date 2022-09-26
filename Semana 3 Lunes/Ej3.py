num= input("Escribe un numero entero positivo: ")
aux = 1
# n*2-1
if num.isnumeric():
    num= int(num)
    num= num + 1
    for index in range(1,num,2):
        while num >= 1:
            if num == 1:
                print(num*2-1)
            else:
                print(num, end=" ")
                num -=2

else:
     print("input error")  