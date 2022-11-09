def suma(n1, n2):
    result_suma = round((n1 + n2), 2)
    return result_suma

def multiplicacion(n1, n2):
    result_multipli = round((n1 * n2), 2)
    return result_multipli

numero_1 = float(input("Escribe un numero: "))
numero_2 = float(input("Escribe otro numero: "))

result_suma = suma(numero_1, numero_2)
print(f"Al sumar {numero_1} + {numero_2} da: {result_suma}")

result_multipli = multiplicacion(numero_1, numero_2)
print(f"Al multiplicar {numero_1} x {numero_2} da: {result_multipli}")

doble = lambda n: n*2
print(f"El doble de 5 es: {doble(5)}")