from sympy import isprime

n1 = int(input("Introduzca el primer numero \n"))
n2 = int(input("Introduzca el segundo numero \n"))

for i in range(n1, n2):
    if isprime(i):
        print(i)
