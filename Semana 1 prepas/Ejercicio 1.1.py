#imprimir saldo inicial
saldo = 3480
print(f"2020/04/10: Saldo inicial es de ${saldo}")
# Se hace una compra de $96 en una tienda
fondo_retirado = 96
print(f"2020/04/11: Se han retirado ${fondo_retirado}")
# Mostrar saldo actual, luego de la compra
saldo = saldo - fondo_retirado
print(f"Saldo actual es de ${saldo}")
salario = 1200
print(f"2020/04/17: Se han recibido ${salario}")
# Mostrar saldo actual, luego de recibir el salario
saldo = saldo + salario
print(f"Saldo actual es de ${saldo}")
#se cobra el 3% del saldo de la cuenta por intereses
print(f"2020/04/30: Se ha cobrado un 3% de intereses sobre la cuenta, de ${round((saldo * 0.03),2)}")
saldo = saldo - (round((saldo * 0.03),2))
print(f"Saldo actual es de ${saldo}")
# se hace una compra en el supermenrcado de $51
fondo_retirado = 51
print(f"2020/05/02: Se han retirado ${fondo_retirado}")
saldo = saldo - fondo_retirado
print(f"Saldo actual es de ${saldo}")