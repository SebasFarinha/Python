class Automovil:
    def __init__(self, modelo, marca, color) :

        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.estado = 'en reposo'
        self.motor = Motor(cilindros=4)

    def acelerar(self, tipo= 'despacio'):
        if tipo == 'rapido':
            self.motor.inyecta_gasolina(10)
        else:
             self.motor.inyecta_gasolina(3)
        self.estado = 'en movimiento'
    
    def get_info_auto(self):
        return f"Modelo: {self.modelo}, Marca: {self.marca}, Color: {self.color}, Estado: {self.estado}, "


    

class Motor:
    def __init__(self, cilindros, tipo = 'diesel'):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 95
    def inyecta_gasolina (self, cantidad):
        self.cantidad = cantidad
        if cantidad == 10:
            self.temperatura = 110
        else:
            self.temperatura = 90

    def get_info_del_motor(self):
        return f"Cilindros: {self.cilindros}, tipo: {self.tipo}, temperatura: {self.temperatura}"




if __name__ == "__main__":
    mi_motor = Motor(6,'nafta')

    mi_auto = Automovil("Supra", "Toyota", "Naranja")
    mi_auto.motor = mi_motor




    mi_auto.acelerar('rapido')


    print(mi_auto.get_info_auto())
    print(mi_motor.get_info_del_motor())








