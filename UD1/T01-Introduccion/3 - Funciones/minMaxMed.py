def calc(l):
    min = l[0]
    max = l[0]
    suma = 0

    if not lista:
        print("La lista esta vacia")
        return False
    else:
        for i in l:
            if i < min:
                min = i
            if i > max:
                max = i
            suma += i
            med = suma / len(l)
        return min, max, med
        


lista = [1,2,3,4,5]


resultado = calc(lista)
print(resultado)











    
            
