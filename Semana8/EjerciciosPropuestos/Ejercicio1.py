'''Ejercicio 1: Vehículo pt.1
A partir del siguiente diagrama de clases, implementá
clases y métodos para mostrar atributos(ver pdf)'''

class Vehiculo:
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas

    def __str__(self):
        return f'COLOR: {self.color}\nRUEDAS: {self.ruedas}'
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad,cilindrada):
        super().__init__(color, ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return f'{super().__str__()} \nVELOCIDAD: {self.velocidad} km/h\nCILINDRADO: {self.cilindrada} cc.'
    

if __name__=='__main__':

    alfa_romeo=Coche('Amarello',4,298,600)
    print(alfa_romeo)

