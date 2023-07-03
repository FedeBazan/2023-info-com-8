'''
Ejercicio 7:Bebidas Online

Vamos a administrar un ecommerce de bebidas.
En un depósito se guardan las bebidas a comercializar.
Estos productos son bebidas como agua mineral y gaseosas.
De los productos nos interesa saber su identificador(cada uno tiene uno distinto), cantidad
de litros, precio y marca.
Si es agua mineral nos interesa saber también el origen (Manantial,Ciudad,etc).
Si es una gaseosa queremos saber el porcentaje que tiene de azúcar y si tiene alguna promoción
(si la tiene tendrá un descuento del 1'% en el precio).
Las operaciones del almacén son las siguientes:
    +Calcular precio de todas las bebidas: calcula el precio total de todos los
    productos del almacén
    *Calcular el precio total de una marca de bebida: dada una marca, calcular el precio
    total de esas bebidas.
    *Agregar producto: agrega un producto, si el identificador esta repetido en
    alguno de las bebidas, no se agregará esa bebida.
    *Eliminar un producto: dado un ID, eliminar el producti del depósito.
    *Mostrar indormación: mostramos para cada bebida toda su información.
    

'''

class Bebida:
    def __init__(self, id, litros, precio, marca):
        self.id = id
        self.litros = litros
        self.precio = precio
        self.marca = marca

    def __str__(self) -> str:
        return f'MARCA: {self.marca}\nLITROS: {self.litros}\nPRECIO: {self.precio}'


class Agua_Mineral(Bebida):
    def __init__(self, id, litros, precio, marca, origen):
        super().__init__(id, litros, precio, marca)
        self.origen = origen

    def __str__(self) -> str:
        return f'{super().__str__()}\nORIGEN: {self.origen}'


class Gaseosa(Bebida):
    def __init__(self, id, litros, precio, marca, porcentaje_azucar, descuento):
        super().__init__(id, litros, precio, marca)
        self.porcentaje_azucar = porcentaje_azucar
        self.descuento = descuento

    def __str__(self) -> str:
        return f'{super().__str__()}\nPORCENTAJE AZUCAR: {self.porcentaje_azucar}\nOFERTA: {self.descuento}'


class Almacen:
    def __init__(self):
        self.bebidas = []

    def calcular_precio_total(self):
        total = sum(bebida.precio for bebida in self.bebidas)
        return total

    def calcular_precio_marca(self, marca):
        total = sum(bebida.precio for bebida in self.bebidas if bebida.marca == marca)
        return total

    def agregar_bebida(self, bebida):
        if bebida.id in [b.id for b in self.bebidas]:
            print("Error: El identificador ya existe.")
        else:
            self.bebidas.append(bebida)
            print("Bebida agregada correctamente.")

    def eliminar_bebida(self, id):
        bebida_encontrada = None
        for bebida in self.bebidas:
            if bebida.id == id:
                bebida_encontrada = bebida
                break

        if bebida_encontrada:
            self.bebidas.remove(bebida_encontrada)
            print(f"Bebida con ID {id} eliminada correctamente.")
        else:
            print("Error: No se encontró una bebida con ese ID.")

    def mostrar_informacion(self):
        if self.bebidas:
            for bebida in self.bebidas:
                print(bebida)
                print("-------------------------")
        else:
            print("El almacén está vacío.")


'''
Se debe desarrollar un menu y organizar las ordenes

agua_mineral = Agua_Mineral(1, 1.5, 10, "Manantial", "Nestlé")
gaseosa = Gaseosa(2, 0.5, 15, "Coca-Cola", 10, True)

almacen = Almacen()
almacen.agregar_bebida(agua_mineral)
almacen.agregar_bebida(gaseosa)
almacen.mostrar_informacion()

print("Precio total de todas las bebidas:", almacen.calcular_precio_total())
print("Precio total de las bebidas de la marca Coca-Cola:", almacen.calcular_precio_marca("Coca-Cola"))

almacen.eliminar_bebida(1)
almacen.mostrar_informacion()

''' 