class Dni():
    def __init__(self, cadena=""):
        self.dni = cadena
        self.numeroSano = False
        self.letra = False

    def setDni(self, cadena):
        self.dni = cadena

    def getDni(self):
        return self.dni

    def getNumeroSano(self):
        return self.numeroSano
    
    def getLetraSana(self):
        return self.letra
    
    def checkDni(self):

    def checkLetra(self):


    def checkCIF(self):
        return self.checkDni() and self.checkLetra()