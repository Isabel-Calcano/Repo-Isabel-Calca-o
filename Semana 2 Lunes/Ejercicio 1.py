from operator import truediv


numero1= input("Escriba el primer numero: ")
numero2=  input("Escriba el segundo numero: ")
is_valid = True

if numero1.isnumeric():
    numero1= float(numero1)
else:
     is_valid = False

if numero2.isnumeric():
    numero2= float(numero1)
else:
     is_valid = False

if is_valid:
    print(numero1/numero2)