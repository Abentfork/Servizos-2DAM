from collections import defaultdict
from optparse import Option


agenda = defaultdict(list)
opcion = int

while opcion != 0:
    opcion = int(input("Introduzca una opcion (1.- añadir 2.- buscar)\n"))
    if opcion == 1:
        nombre = input("Introduce el nombre\n")
        nT = int(input("Cuantos numeros quiere añadir\n"))
        for i in range(0,nT):
            agenda[nombre.lower].append(input(f"Introduzca el {i + 1}º numero de telefono "))

    if opcion == 2:
        nombre = input("Introduce el nombre que quieres buscar\n").lower
        print(f"{nombre}:\n")
        for i in agenda[nombre]:
            print(f"  {i}")
