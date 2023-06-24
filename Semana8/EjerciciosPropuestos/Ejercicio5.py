'''
Ejercicio 5: Gestion de Donaciones

Nos piden que diseñemos un programa para gestionar donaciones de alimentos.
Los productos tienen los siguientes atributos:
    *Nombre
    *Cantidad
Tenemos dos tipos de productos:
    *Perecedero: tiene un atributo llamado días a caducar.
    *No perecedero: tiene un atributo llamado tipo.
Tendremos una funcion llamada Calcular, que segun cada clase hara una cosa u otra
otra, a esta funcion se le envia la cantidad por producto y entidades a las cuales
se entregaran donaciones.
    *Debe obtener la cantidad que se enviara a cada enidad, sabiendo que la distri
    bucion debe ser lo mas equitativa posible.En caso que sobren productos, se almacenan
    para el próximo ciclo de donación
    +Además si el producto es perecedero, se informará:
        +Si le queda menos de 10 días para caducar, la entrega debe hacerse en el 
        día actual
        +Si le queda 1 mes para caducar, la entrega debe hacerse en el ploazo de 1 semana.
    +Si fuera No Perecedero, se informa cuántos productos se entregarán por entidad
    y que queda libre la elección de la fecha de entrega siempre que no supere el mes.
'''

class Producto:
    def __init__(self,nombre,cantidad):
        self.nombre=nombre
        self.cantidad=cantidad

    def __str__(self):
        return f'NOMBRE DEL PRODUCTO: {self.nombre}\nCANTIDAD: {self.cantidad}'
    
class Perecedero(Producto):
    def __init__(self, nombre, cantidad,dias_a_caducar):
        super().__init__(nombre, cantidad)
        self.dias_a_caducar=dias_a_caducar
    
    def __str__(self):
        return f'{super().__str__()} \nDIAS A CADUCAR: {self.dias_a_caducar} días'
        #return f'NOMBRE DEL PRODUCTO: {self.nombre}\nCANTIDAD: {self.cantidad}\nDIAS A CADUCAR: {self.dias_a_caducar} días'
    
class No_Perecedero(Producto):
    def __init__(self, nombre, cantidad,tipo):
        super().__init__(nombre, cantidad)
        self.tipo=tipo
    
    def __str__(self):
        return f'{super().__str__()} \nTIPO: {self.tipo}'
    
def calcular(cantidad,entidades):
    print (f'Se debe repartir {cantidad//entidades} productos entre las {entidades} entidades.')
    if cantidad%entidades > 0:
        print(f'Sobran {cantidad%entidades} productos, se almacenarán para la proxima donacion')
        
def calcular_perecederos(cantidad,entidades):
    calcular(cantidad,entidades)
    if dias<10:
        print (f'La entrega debe hacerce HOY.')
    elif dias>28:
        print (f'La entrega debe hacerse en el plazo de 1 semana.')

def calcular_no_perecederos(cantidad,entidades):
    calcular(cantidad,entidades)
    dias=int(input('¿En cuantos dias el producto será entregado? Se recominda antes de 28 dias: '))
    while dias>28:
        print ('FATAL ERROR'.center(50,'*'))
        print('Los días no deben superar 28 dias para entrega')
        dias=int(input('¿En cuantos dias el producto será entregado? Se recominda antes de 28 dias: '))
    print(f'La entrega del producto se programó para dentro de {dias} dias')    



print('BIENVENIDO'.center(50,'*'))
opc=int(input('Elija la opcion de alimento a donar\n1- Alimento PERECEDERO\n2-Alimento NO PERECEDERO\n'))
entidades=int(input('¿A cuantas entidaes será donado el producto?: '))
nombre=input('Nombre dle producto: ')
cantidad=int(input('Cantidad: '))

if opc==1:
    dias=int(input('Indica cuantos dias quedan para que caduque el producto: '))
    producto=Perecedero(nombre,cantidad,dias)
    calcular_perecederos(cantidad,entidades,dias)
    print(producto)
elif opc==2:
    tipo=input('Indica tipo de alimento: ')
    producto=No_Perecedero(nombre,cantidad,tipo)
    calcular_no_perecederos(cantidad,entidades)
    print(producto)
else:
    print('Error, opcion invalida')