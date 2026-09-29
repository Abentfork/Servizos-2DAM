
from functools import reduce


lista = [1,2,3,4,5]

resultado = reduce(lambda a, b : a + b, lista )
print(resultado)