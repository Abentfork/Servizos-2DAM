a = open("T01-Introduccion/5 - Ficheros/1.txt", "r",encoding="utf8")

archivo = a.read()

nLines = len(archivo.split("\n"))
nCaracters = len(archivo)
nPalabras = len(archivo.split(" "))

a.close()


print(f"Nº Lineas: {nLines} Nº Caracteres: {nCaracters} Nº Palabras: {nPalabras}")


    
