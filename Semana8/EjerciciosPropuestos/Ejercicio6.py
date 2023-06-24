'''
Ejercicio 6: Cuentas Electrónicas

Crea una clase llamada CUENTA que tendrá los siguientes atributos: titular(que es una persona)
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
        return f'NOMBRE DEL TITULAR: {self.titular}\nCANTIDAD DEL FONDO:$ {self.cantidad}'
    
    def ingresar(self,cantidad):
        if cantidad>0:
            self.cantidad+=cantidad
        return self.cantidad
    
    def retirar(self,cantidad):
        self.cantidad-=cantidad
        return self.cantidad
    
print('BIENVENIDO'.center(50,'*'))
titular=input('Ingrese el nombre del titular de la cuenta: ')
efectivo=float(input('Ingrese la cantidad de efectivo en la cuenta: '))
cliente=Cuenta(titular,efectivo)
print(''.center(50,'='))
print(cliente) # cliente.mostrar_datos()
print('MENU'.center(50,'='))
opc=0
while opc!=3:

    print('''Seleccione La accion que quiere realizar:
    1-Ingresar Efectivo
    2-Retirar Efectivo
    3-Salir
    
    ''')
    opc=int(input(''))
    if opc==1:
        dinero=float(input('Ingrese la cantidad de dinero: '))
        cliente.cantidad=cliente.ingresar(dinero)
    elif opc==2:
        dinero=float(input('Ingrese la cantidad a retirar: '))
        cliente.cantidad=cliente.retirar(dinero)
    print(''.center(50,'='))
    print(cliente)
    print(''.center(50,'='))
