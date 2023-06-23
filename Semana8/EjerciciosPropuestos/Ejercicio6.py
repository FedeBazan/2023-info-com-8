'''
Ejercicio 6: Cuentas Electrónicas

Crea una clase llamada que tendrá los siguientes atributos: titular(que es una persona)
y cantidad (puede tener decimales). Ek titukar será obligatoria y la cantidad es opcional.
Implementa los siguientes métodos:
    *nostrar():Muestra los datos de la cuenta.
    *Ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida
    es negativa, no se hará nada.
    *retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en
    números rojos.
'''

class Cuenta:
    def __init__(self,titular,cantidad):
        self.titular=titular
        self.cantidad=cantidad
    
    #__str__ será la funcion mostrar
    def __str__(self):
        return f'NOMBRE DEL TITULAR: {self.titular}\nCANTIDAD DEL FONDO:{self.cantidad}'
    
    def ingresar(self,cantidad):
        if cantidad>0:
            self.cantidad+=cantidad
            return self.cantidad
    
    def retirar(self,cantidad):
        self.cantidad-=cantidad
        return self.cantidad
    
#hacer un menu para desarrollar