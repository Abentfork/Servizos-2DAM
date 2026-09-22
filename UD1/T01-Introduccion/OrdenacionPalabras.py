frase = input("Introduzca una frase \n").split(" ")

print(f"Alfabeticamente: {sorted(frase)} Longitud: {sorted(frase, key=len)}")