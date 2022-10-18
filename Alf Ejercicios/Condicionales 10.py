# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.

#           Ingredientes vegetarianos: Pimiento y tofu.
#           Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

ing_veg = ["Pimiento", "Tofu"]
ing_no_veg = ["Peperoni", "Jamón", "Salmón"]

tipo = input("¿Que tipo de pizza quiere? \nEscriba 'v' para vegetariana o 'n' para no vegetariana \n--> ")
tipo = tipo.lower()

if tipo == "v":
    ingrediente = input("""Ha elejido la opcion vegetariana.
    La pizza incluye por defecto tomate y queso mozzarela.
    Elija uno de los siguientes ingredientes: 
    'p' para pimiento
    't' para tofu
    --> """)
    ingrediente = ingrediente.lower()
    if ingrediente == "p":
        print("Una vez sea procesado su pago, su pizza vegetariana de pimiento estará en camino")
    elif ingrediente == "t":
        print("Una vez sea procesado su pago, su pizza vegetariana de tofu estará en camino")
    else:
        print("No se introdujo el dato correctamente, por favor intente de nuevo")
elif tipo == "n":
    ingrediente = input("""ha elejido la opcion no vegetariana.
    La pizza incluye por defecto tomate y queso mozzarela .
    Elija uno de los siguientes ingredientes: 
    'p' para peperoni
    'j' para jamón
    's' para salmón
    --> """)
    ingrediente = ingrediente.lower()
    if ingrediente == "p":
        print("Una vez sea procesado su pago, su pizza no vegetariana de peperoni estará en camino")
    elif ingrediente == "j":
        print("Una vez sea procesado su pago, su pizza no vegetariana de jamón estará en camino")
    elif ingrediente == "s":
        print("Una vez sea procesado su pago, su pizza no vegetariana de salmón estará en camino")
    else:
        print("No se introdujo el dato correctamente, por favor intente de nuevo")
else:
    print("No se introdujo el dato correctamente, por favor intente de nuevo")
