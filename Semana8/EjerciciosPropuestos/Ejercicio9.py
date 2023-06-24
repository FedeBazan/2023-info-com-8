'''
Ejercicio 9: Cafetera robot

Como diseñariamos el comportamiento de una cafetera robot?
Desarrolla una clase Cafetera con atributos:
    + _capacidadMaxima (la cantidad máxima de café que puede contener la cafetera)
    + _cantidadActuak (la cantidad actual de café que hay en la cafetera).
Luego desarrollar los siguientes métodos:
    * llenarCafetera():pues eso, hace que la cantidad actual sea igualo a la capacidad.
    * servirTaza(int): simula la acción de servir una taza con la capacidad indicada.
    Si la cantidad actual de café "no alcanza" para llenar la taza, se sirve lo que quede.
    *vaciarCafetera(): pone la cantidad de café actual en cero.
    *agregarCafe(int): añade a la cafetera la cantidad de café indicada.
'''

class Cafetera:
    def __init__(self,capacidad_maxima,cantidad_actual):
        self.capacidad_maxima=capacidad_maxima
        self.cantidad_actual=cantidad_actual

    def __str__(self) -> str:
        return f'CAPACIDAD MAXIMA: {self.capacidad_maxima}\nCANTIDAD ACTUAL:{self.cantidad_actual}'
    
    def llenar_cafetera(self):
        if self.cantidad_actual<self.capacidad_maxima:
            self.cantidad_actual=self.capacidad_maxima
        return self.cantidad_actual

    def servir_taza(self,capacidad):
        if self.cantidad_actual>=capacidad:
            print(f'Al cliente se le servira {capacidad}')
            self.cantidad_actual-=capacidad
            return self.cantidad_actual
        elif capacidad>self.cantidad_actual:
            print(f'No hay suficiente cafe,Al cliente se le servira {self.cantidad_actual}')
            self.cantidad_actual=0
            return self.cantidad_actual
        
    def vaciar_cafetera(self):
        self.cantidad_actual=0
        return self.cantidad_actual

    def agregar_cafe(self,cantidad):
        self.cantidad_actual+=cantidad
        return self.cantidad_actual

capacidad_maxima=float(input('Ingrese la capacidad maxima de la cafetera: '))
cantidad_actual=float(input('Ingrese la cantidad actual del cafe en la cafetera: '))

#control de error de variable
while cantidad_actual>capacidad_maxima:
    print ('ERROR'.center(30,'-'))
    print ('valores incorrectos, la cantidad maxima supera la capacidad de la cafetera')
    capacidad_maxima=float(input('Ingrese la capacidad maxima de la cafetera: '))
    cantidad_actual=float(input('Ingrese la cantidad actual del cafe en la cafetera: '))

pedido=Cafetera(capacidad_maxima,cantidad_actual)

#Manejo de Menu
opc='0'
while opc!='5':
    print ('''Seleccione la opcion que desea realizar:
    1-Llenar la cafetera
    2-Servir Taza
    3-Vaciar cafetera
    4-Agregar Cafe
    5-Salir
    ''')
    opc=input(' ')

    if opc=='1':
        pedido.cantidad_actual=pedido.llenar_cafetera()
    elif opc=='2':
        capacidad=float(input('Ingrese la cantidad para la taza: '))
        cantidad_actual=pedido.servir_taza(capacidad)
    elif opc=='3':
        print ('Se va a vaciar la cafetera')
        cantidad_actual=pedido.vaciar_cafetera()
    elif opc=='4':
        cafe=float(input('Ingrese la cantidad de cafe que desea agregar: '))
        test=cantidad_actual+cafe
        while test>capacidad_maxima:
            print ('ERROR'.center(20,'-'))
            cafe = float(input('Ingrese la cantidad de cafe que desea agregar: '))
            test=cantidad_actual+cafe
        cantidad_actual=pedido.agregar_cafe(cafe)
    
    print('='.center(50,'='))
    print(pedido)
    print('='.center(50,'='))