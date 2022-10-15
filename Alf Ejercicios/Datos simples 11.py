#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al 
# balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad 
# de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa 
# debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.

interes = 0.04

saldo = float(input("Cuanto dinero hay depositado en la cuenta? "))
saldo_1 = round(saldo + (saldo * interes) , 2)
saldo_2 = round(saldo_1 + (saldo_1 * interes) , 2)
saldo_3 = round(saldo_2 + (saldo_2 * interes) , 2)

print(f"Tras el primer año, la cantidad de ahorros estará en {saldo_1}")
print(f"Tras el segundo año, la cantidad de ahorros estará en {saldo_2}")
print(f"Tras el tercer año, la cantidad de ahorros estará en {saldo_3}")