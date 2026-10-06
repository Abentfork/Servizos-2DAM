class Empleado():
    def __init__(self,nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    def __str__(self):
        return f"Nombre: {self.nombre} Sueldo: {self.sueldo} "
        
        
        
class Gerente(Empleado):
    def __init__(self, nombre, sueldo,departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento
    def __str__(self):
        return f"super().__str__() Departamento: {self.departamento}"
        

class Programador(Empleado):
    def __init__(self, nombre, sueldo, lenguaje):
        super().__init__(nombre, sueldo)
        self.lenguaje = lenguaje
    def __str__(self):
        return f"{super().__str__()} Lenguaje: {self.lenguaje}"
        
        


p = Programador("juan",10.99,"Java")

print(p)