medications = {
        "prescription": {
            "antibiotics": {
                "skin": [
                    {
                        "id": 1,
                        "name": "Clindamicine",
                        "price": 300
                    },
                    {
                        "id": 2,
                        "name": "Cefadroxil",
                        "price": 350
                    },
                    {
                        "id": 3,
                        "name": "Amoxicillin",
                        "price": 320
                    }
                ],
                "respiratory-system":[
                    {
                        "id": 4,
                        "name": "Citromicine",
                        "price": 380
                    },
                    {
                        "id": 5,
                        "name": "Levofloxacine",
                        "price": 125
                    },
                    {
                        "id": 6,
                        "name": "Azitromicine",
                        "price": 740
                    }
                ]
            },
            "analgesic": {
                "anti-inflammatories": [
                    {
                        "id": 7,
                        "name": "HYDROCODONE-IBUPROFEN",
                        "price": 150
                    },
                    {
                        "id": 8,
                        "name": "IBUDONE",
                        "price": 180
                    }
                ]
            }
        },
        "non-prescription": {
            "analgesic": {
                "general": [
                    {
                        "id": 9,
                        "name": "Acetaminophen",
                        "price": 15
                    },
                    {
                        "id": 10,
                        "name": "Ibuprofen",
                        "price": 20
                    }
                ]
            },
            "antihistamine": {
                "antiallergic": [
                    {
                        "id": 11,
                        "name": "Loratadine",
                        "price": 12
                    },
                    {
                        "id": 12,
                        "name": "Desler M",
                        "price": 8
                    },
                    {
                        "id": 13,
                        "name": "Allegra",
                        "price": 21
                    },
                    {
                        "id": 14,
                        "name": "Fexofenadine",
                        "price": 18
                    }
                ]
            }
        }
    }

print("***** Welcome to Saman-Labs ***** \n Please select one of the following options:")
opcion= int(input("1- Show inventory \n2- Purchase \n3- Exit \n--> "))

while True:
    if opcion == 1:
        print("Inventory:")
    elif opcion == 2:
        print("Purchase proccess:")
    elif opcion == 3:
        print("Thank you for your patronage. \n Goodbye.")
    else:
        print("Select one of the shown options")
    break

#Kind = prescription// non-prescription
#medication = antibiotics, analgesic // analgesic, antihistamine
#funcion = skin, respiratory system / anti-inflamatory // genersal / antialergic
#Data = 
for prescripcion, antibiotics in medications.items():
    for i in medications.items():
        print(medications, medications[i])
        for specific_data in .items():
            print("""From {} medications, there are available:
    {}""".format(i,medications))
