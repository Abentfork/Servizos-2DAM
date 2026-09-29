from collections import defaultdict


dic = {"hola" : "adios", "ven" : "vete"}


inverso = {valor : clave for clave, valor in dic.items()}

print(inverso)