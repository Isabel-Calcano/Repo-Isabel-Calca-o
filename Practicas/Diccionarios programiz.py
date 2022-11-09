persona = {"nombre": "Alejandro", "Edad": 20}

# dato = key
for dato in persona:
    print(f"{dato}:\t {persona[dato]}")
    
print()

persona["nombre"] = "Beatriz"
persona["Edad"] = 40
persona["Oficio"] = "escritora"

for dato in persona:
    print(f"{dato}:\t {persona[dato]}")