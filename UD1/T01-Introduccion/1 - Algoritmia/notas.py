from collections import defaultdict


notas = defaultdict(int)
entrada = ""

while entrada != "fin":
    entrada = input("Introduzca el nombre del alumno \n")
    if entrada == "fin":
        break

    notas[entrada] = input("Introduzca la nota del alumno \n")

print("Notas alumnos\n------------------")
for alumno in notas:
    print(f"{alumno} : {notas[alumno]} \n")
