from collections import defaultdict


frase = input("Introduce una frase\n").split(" ")
frecuencia = defaultdict(int)

for i in frase:
    frecuencia[i.lower()] += 1

print(frecuencia)


