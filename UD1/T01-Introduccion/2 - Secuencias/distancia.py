import math


coordenadas = {}

coordenadas["x1"] = int(input("Introduzca x1 \n"))
coordenadas["y1"] = int(input("Introduzca y1 \n"))
coordenadas["x2"] = int(input("Introduzca x2 \n"))
coordenadas["y2"] = int(input("Introduzca y2 \n"))


distancia = math.sqrt((coordenadas["x2"] - coordenadas["x1"])**2 + (coordenadas["y2"] - coordenadas["y1"])**2)

print(f"La distancia es: {distancia}")



