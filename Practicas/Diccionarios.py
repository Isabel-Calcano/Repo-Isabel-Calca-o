nombres= {'1': 'Jose', '2': 'Maria', '3': 'Alberto'}
print(nombres['1'])

#agregar un nombre en una posicion:
nombres['3'] = 'Beatriz'
print(nombres['3'])

#revisar si un elemento esta dentro del diccionario:
print('5' in nombres)
print('2' in nombres)
print(nombres.get('5',))
print(nombres.get('5', 'no existe'))

for numero, nombre in nombres.items():
    print('el numero {} es {}'.format(numero, nombre))

print(nombres.get(6) is None)
print(nombres.get(6) is not None)