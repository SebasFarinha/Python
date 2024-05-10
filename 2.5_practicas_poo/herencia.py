class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado) 



if __name__ == "__main__":
    rect = Rectangulo(8,5)
    print(rect.area())

    cuadrado = Cuadrado(6)
    print(cuadrado.area())
        