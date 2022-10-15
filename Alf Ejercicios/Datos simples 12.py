# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el 
# programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser 
# fresca y el coste final total.

precio = 3.49
precio_descuento = round(3.49 * 0.4 , 2)

pan_vendido_ayer = int(input("Cuantas barras de ayer se quieren comprar? "))
print("Una barra de pan fresca cuesta {0}€".format(precio))

total = pan_vendido_ayer * precio_descuento

print(f"""Se quieren comprar {pan_vendido_ayer} barras de pan de ayer
se aplica un descuento de 60%, quedando el precio total a pagar de: {total}€""")