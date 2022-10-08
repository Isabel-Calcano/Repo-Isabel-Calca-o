juegos = {
    "Shooter": [
        {
            "id": 1,
            "name": "Overwatch2",
            "price": 60  
        },
        {
            "id": 2,
            "name": "Valorant",
            "price": 0
        },
        {
            "id": 3,
            "name": "Pixel Gun 3D",
            "price": 10
        }
    ],
    "RPG": [
        {
            "id": 4,
            "name": "Pokemon",
            "price": 50  
        },
        {
            "id": 5,
            "name": "Final Fantasy Exvius",
            "price": 0
        }
    ],
    "Open World": [
        {
            "id": 6,
            "name": "Minecraft",
            "price": 60  
        },
        {
            "id": 7,
            "name": "Cyberpunk 2077",
            "price": 60
        },
        {
            "id": 8,
            "name": "GTA V",
            "price": 40
        }
    ],  
}

print("""**** Bienvenido a la tienda colaborativa de 'Metro-Steam' y 'Epic Saman' ****
Por favor elija una de las siguientes opciones:""")
opcion= input("1- Ver lista de juegos \n 2- Comprar juego \n 3-salir \n-->")

while True:
    if opcion == 1:
        print("lista de juegos")
    elif opcion == 2:
        print("Comprar")
    elif opcion == 3:
        print("salir")
    else:
        print("Selecciona una de las opciones:")
    break
        
for tipos in juegos:
    print

