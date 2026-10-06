class Rectangulo():
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto
        
    def area(self):
        return self.alto * self.ancho
    
    def perimetro(self):
        return (self.ancho * 2) + (self.alto * 2)
        


a = Rectangulo(2, 3)

print(a.area())
print(a.perimetro())