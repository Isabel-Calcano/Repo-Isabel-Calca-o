class Persona:

    # Constructor de la clase
    def __init__(self, nombre, edad):
        self.name = nombre
        self.years_old = edad

    # Procedimientos y metodos de la clase
    def cumplir_año(self):
        self.years_old += 1
        print("haz cumplido un año")
