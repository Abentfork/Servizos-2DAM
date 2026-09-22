from collections import defaultdict
frase = list(input("Introduzca una Frase \n"))

letras = defaultdict(int)

for n in frase:
    if n.isalpha():
        letras[n.lower()] += 1


print(sorted(letras.items()))

