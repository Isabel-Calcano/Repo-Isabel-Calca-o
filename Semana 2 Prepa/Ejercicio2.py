estudiantes = ["Andres", "Maria", "Isabel"]

for estudiante in estudiantes:
    print(estudiante)

print(" ")

for i in range(1, len(estudiantes) + 1):
    print(estudiantes[-i])

estudiantes.append(input("nombre de un estudiante: "))
print(estudiantes)