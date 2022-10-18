renta = input("Indique su renta anual: ")

renta = round(float(renta), 2)

if renta < 10000:
    tipo = 5

elif renta < 20000:
    tipo = 15

elif renta < 35000:
    tipo = 20

elif renta < 60000:
    tipo = 30

else:
    tipo = 45

print(f"Su tipo es de {tipo}%, debe pagar $", round((renta * tipo / 100), 2))