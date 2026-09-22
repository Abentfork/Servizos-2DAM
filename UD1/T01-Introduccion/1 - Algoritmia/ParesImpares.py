numeros = input("Introduzca una lista de numeros separados por espacios\n").split(" ")
pares = []
impares = []

for n in numeros:
    if int(n) % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"Pares: {pares} \n Impares: {impares}")

