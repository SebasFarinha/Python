class Calculadora:
    Numero1 = None
    Numero2 = None
    Resultado=None
    Historial=None
    def __init__(self,n,m):
        self.Numero1 = n
        self.Numero2 = m
        self.Resultado=0
        self.Historial = []
    
    def sumar (self):
        return self.Numero1 + self.Numero2
    def restar (self):
        return self.Numero1 - self.Numero2
    def multiplicar (self):
        return self.Numero1 * self.Numero2

    '''def set_valores(self,x,y):
        Numero1 = x
        Numero2 = y'''


if __name__ =="__main__":

    suma1=Calculadora(88,12)
    print("La Suma es: ", suma1.sumar())


    resta1= Calculadora(50,45)
    print("La resta es: ", resta1.restar())


    print("La multiplicación es: ", resta1.multiplicar())   

    
