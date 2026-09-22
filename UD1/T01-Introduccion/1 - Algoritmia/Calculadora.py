n1 = int(input("Introduzca el primer numero \n"))
n2 = int(input("Introduzca el segundo numero \n"))
operacion = input("Introduzca una operacion (+,-,*,/) \n")

if operacion == "+":
    print(n1 + n2)
elif operacion == "-":
    print(n1 - n2)
elif operacion == "*":
    print(n1 * n2)
else:
    print(n1 / n2)