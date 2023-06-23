'''
Ejercicio 2 : Vehiculo pt.2
**Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehículos.
**Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra mostrando el nombre
de su clase y sus
atributos.
**Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas
concuerde con el valor del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el
argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
'''

from Ejercicio1 import *

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada,carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga=carga

    def __str__(self):
        return f'{super().__str__()}\nCarga: {self.carga} Kg. '

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)
        self.tipo=tipo

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo,velocidad,cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

if __name__ == '__main__':
    carro=Vehiculo('Negro',6)
    volkwagen=Coche('Verde',4,220,400)
    mercedez=Camioneta('Morado',4,200,250,200)
    bmx=Bicicleta('Gris',2,'Montaña')
    rx=Motocicleta('NEgro/Rojo',2,'Pistera',320,1200)
    
    def catalogar(vehiculos,num_ruedas):
        num_coincidencia=0
        for rodado in vehiculos:
            print('----------')
            print(rodado)
            if rodado.ruedas==num_ruedas:
                num_coincidencia+=1
        print (f'Se han encontrado {num_coincidencia} vehículos con {num_ruedas} ruedas:')
    vehiculos=(carro,volkwagen,mercedez,bmx,rx)
    num_ruedas=int(input('Coloque el numero de ruedas para analizar: '))
    catalogar(vehiculos,num_ruedas)