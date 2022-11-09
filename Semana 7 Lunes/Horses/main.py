from Horse import horse
from Valids import valid
from Race import race

def main():
    print("Welcome to Derby sjakaidjm")
    valids = int(input("Please enter how many valids will occur: "))
    races = int(input("Please enter how many races will happen in each valid: "))
    horse1 = horse("El rayo veloz", 1)
    horse2 = horse("Gustavo", 2)
    horse3 = horse("El caballo maravilla", 3)
    horse4 = horse("Superman", 4)
    horse5 = horse("El caballo random", 5)
    horse6 = horse("El mas crack", 6)
    for valid in range(valids):
        race_list = []
        horse_list = [horse1, horse2, horse3, horse4, horse5, horse6]
        for race in range(races):
            race_list.append()


main()