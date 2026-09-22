import random


numero = random.randint(1, 100)


while intento != numero:
    intento = int(input("Introduzca su intento (1 - 100)"))
    if intento > numero:
        print("El numero introducido es mayor")
    else:
        print("El numero introducido es menor")

print("Enhorabuena has adivinado")