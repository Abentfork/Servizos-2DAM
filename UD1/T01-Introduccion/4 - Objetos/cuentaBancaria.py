class cuenta:
    def __init__(self, saldo):
        self.saldo = float(saldo)
        
        
    def ingresar(self, ingreso):
        self.saldo = self.saldo + ingreso
        return True
    
    def retirar(self, retirada):
        
        
        if self.saldo < retirada:
            return False
        else:
            self.saldo = self.saldo - retirada
            return True