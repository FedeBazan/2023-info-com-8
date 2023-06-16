'''
Ejercicio 4: Tiempo
Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser
instanciada indicando: los tres atributos, sólo la hora y minuto, o sólo la hora.
Crear además los métodos necesarios para modificar la hora en cualquier
momento de forma manual. Mantenga la integridad de los datos en todo
momento definiendo de tipo “private”. Crear una clase prueba_tiempo que
prueba una hora concreta y la modifique a su gusto mostrándola por pantalla.

'''
import datetime
import re

'''
class Tiempo:
    def __init__(self, hora, minuto=0, segundo=0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def modificar_hora(self, hora, minuto=0, segundo=0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def obtener_hora(self):
        return self.__hora

    def obtener_minuto(self):
        return self.__minuto

    def obtener_segundo(self):
        return self.__segundo
'''

class PruebaTiempo:
    def __init__(self):
        self.tiempo = datetime.datetime.now()  # Obtener la hora actual

    def modificar_tiempo(self):
        hora = self.__ingresar_hora()
        minuto = self.__ingresar_minuto()
        segundo = self.__ingresar_segundo()
        self.tiempo = self.tiempo.replace(hour=hora, minute=minuto, second=segundo)  # Modificar la hora

    def __ingresar_hora(self):
        hora = int(input("Ingrese la hora: "))
        while not (0 <= hora <= 23):
            print("El valor de la hora debe estar entre 0 y 23.")
            hora = int(input("Ingrese la hora nuevamente: "))
        return hora

    def __ingresar_minuto(self):
        minuto = int(input("Ingrese el minuto: "))
        while not (0 <= minuto <= 59):
            print("El valor del minuto debe estar entre 0 y 59.")
            minuto = int(input("Ingrese el minuto nuevamente: "))
        return minuto

    def __ingresar_segundo(self):
        segundo = int(input("Ingrese el segundo: "))
        while not (0 <= segundo <= 59):
            print("El valor del segundo debe estar entre 0 y 59.")
            segundo = int(input("Ingrese el segundo nuevamente: "))
        return segundo

    def mostrar_tiempo(self):
        print(f'Hora: {self.tiempo.hour}:{self.tiempo.minute}:{self.tiempo.second}')




prueba = PruebaTiempo()
prueba.mostrar_tiempo()  # Mostrar la hora inicial
prueba.modificar_tiempo()  # Modificar la hora
prueba.mostrar_tiempo()  # Mostrar la hora modificada