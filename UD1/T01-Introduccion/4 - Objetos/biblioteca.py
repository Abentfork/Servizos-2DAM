class Libro():
    def __init__(self, isbn, nombre, precio):
        self.isbn = isbn
        self.nombre = nombre
        self.precio = precio


class Biblioteca():
    def __init__(self):
        self.libros : list[Libro] = []
    
    def añadirLibro(self, libro):
        if isinstance(libro,Libro):
            self.libros.append(libro)
            return True
        else:
            return False
    
    def buscar(self,nombre):
        for i in self.libros:
            if i.nombre == nombre:
                return i
        
        return False
    
    def listar(self):
        return self.libros

        
        
        
