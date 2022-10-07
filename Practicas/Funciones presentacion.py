
b= float(input("Base del triangulo: "))
a= float(input("Altura del triangulo: "))

def area_triangulo(base, altura):
    return round((base * altura) / 2,2)

print(area_triangulo(b,a))