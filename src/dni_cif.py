class Dni():
    def __init__(self, dni=""):
        self.dni = dni
        self.numero = self._obtenerNumero()
        self.letra = self._obtenerNumero()

    def getDni(self):
        return self.dni
    
    def getNumeroSano(self):
        try:
            return self.numero is int
        except:
            return False

    def getLetraSana(self):
        try:
            return self.letra is str
        except:
            return False
    
    def _obtenerNumero(self):
        try:
            return self.dni[:9]
        except:
            return ''
        
    def _obtenerLetra(self):
        try:
            return list(self.dni)[-1]
        except:
            return ''