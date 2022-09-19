Num= input("write a number: ")

if Num.isnumeric():
    Num= int(Num)
else:
     print("error")

if Num % 2 == 0:
    print(f"The number {Num} is even")
else:
    print(f"The number {Num} is odd")