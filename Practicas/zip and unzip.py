frutas= ['pera', 'manzana', 'fresa']
precio= ['0,50', '0,35', '0,12']
for fruta, bolivar in zip(frutas, precio):
    print('Fruta: {} --> Bs. {}'.format(fruta, bolivar))

inventario= [('manzana', 0.35), ('pera', 0.50), ('fresa', 0.12)]
fruit, price= zip(*inventario)
print(fruit)
print(price)

comidas= ['desayuno', 'almuerzo', 'cena']
for i, comida in enumerate(comidas):
    comidas[i]= comida.title()
    print(comidas[i])