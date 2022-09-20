#REGISTRO DE DATOS BASICOS
# pedir al alumno nombre, apellido, cedula, altura, peso, BMI (Body Mass Index), deporte favorito y promedio de sus calificaciones en su último periodo estudiantil.
print("***Hello dear student*** \n --You'll be asked a few questions pertaining your aplicability to the school's sport programs-- \n --We ask you answer honestly to help garantee a smooth process--")
name = input("please introduce your name: ")
lname = input("please introduce your last name: ")
cedula = input("please introduce your id number: ")
weight = input("please introduce your weight in kg: ")
bmi = input("please introduce your BMI (Body Mass Index): ")
fav_sport = input("please introduce your favorite sport: ")
average_grades = input("please introduce your average grade score from the last school term: ")
# Imprimir los datos en pantalla
print("Here is the data you have introduced so far:")
print(f"Name: {name},{lname}")
print(f"Id number: {cedula}")
print(f"Weight: {weight}")
print(f"BMI: {bmi}")
print(f"Favorite sport: {fav_sport}")
print(f"Average score: {average_grades}")