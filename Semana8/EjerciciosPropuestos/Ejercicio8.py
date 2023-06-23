'''
Ejercicio 8: Mis Libros favoritos
Vamos a crear un programa para nuestros libros favoritos.
Queremos mantener una lista de los libros que hemos ido leyendo, calificando según
nos haya gustado más o menos al leerlo.
    *Para ello, crear la clase Libro, cuyos atributos son el tpitulo, el autor, el número
    de páginas y la calificación que le damos entre 0 y 10.
    *crear los métodos para poder modificar y obtener los atributos si tienen sentido.
    *Posteriormente, crear una clase ConjuntoLibros, que almacena un conjunto de libros.
    Se pueden añadir libros que no existan(siempre que haya espacio), eliminar libros por título 
    o autor, mostrar por pantalla los libros con la mayor y menor calificaci+on dada
    y, por último, mostrar un contenido de todo el conjunto.
'''

class Libro:
    def __init__(self,titulo,autor,num_paginas,calificacion):
        self.titulo=titulo
        self.autor=autor
        self.num_paginas=num_paginas
        self.calificacion=calificacion

    def __str__(self):
        return f'TITULO: {self.titulo}\nAUTOR:{self.autor}\nNUM.PAGINAS;{self.num_paginas}\nCALIFICACION:{self.calificacion}'
    

    def modificar(self):
        print ('MODIFICAR'.center(50,'='))
        self.titulo=input('Ingrese Titulo')
        self.autor=input('Ingrese Autor')
        self.num_paginas=int(input('Ingrese numero de pagias: '))
        self.calificacion=int(input('Ingrese una calificacion entre 0 y 10'))


class ConjuntoLibros:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        if len(self.libros) < 10:
            self.libros.append(libro)
            print("Libro agregado correctamente.")
        else:
            print("Error: No se pueden agregar más libros. El conjunto está completo.")

    def eliminar_libro_por_titulo(self, titulo):
        libros_eliminados = []
        for libro in self.libros:
            if libro.titulo == titulo:
                libros_eliminados.append(libro)

        if libros_eliminados:
            self.libros = [libro for libro in self.libros if libro not in libros_eliminados]
            print(f"Se han eliminado los libros con el título '{titulo}'.")
        else:
            print(f"No se encontraron libros con el título '{titulo}'.")

    def eliminar_libro_por_autor(self, autor):
        libros_eliminados = []
        for libro in self.libros:
            if libro.autor == autor:
                libros_eliminados.append(libro)

        if libros_eliminados:
            self.libros = [libro for libro in self.libros if libro not in libros_eliminados]
            print(f"Se han eliminado los libros del autor '{autor}'.")
        else:
            print(f"No se encontraron libros del autor '{autor}'.")

    def mostrar_libros_mayor_calificacion(self):
        max_calificacion = max(libro.calificacion for libro in self.libros)
        libros_max_calificacion = [libro for libro in self.libros if libro.calificacion == max_calificacion]

        print("Libros con mayor calificación:")
        for libro in libros_max_calificacion:
            print(libro)
            print("-------------------------")

    def mostrar_libros_menor_calificacion(self):
        min_calificacion = min(libro.calificacion for libro in self.libros)
        libros_min_calificacion = [libro for libro in self.libros if libro.calificacion == min_calificacion]

        print("Libros con menor calificación:")
        for libro in libros_min_calificacion:
            print(libro)
            print("-------------------------")

    def mostrar_contenido(self):
        if self.libros:
            for libro in self.libros:
                print(libro)
                print("-------------------------")
        else:
            print("El conjunto de libros está vacío.")


# Ejemplo de uso
print('Bienvenido'.center(50,'*'))

'''
Completar con un menu y hacerlo mas dinamico al programa
conjunto_libros = ConjuntoLibros()

libro1 = Libro("El gran Gatsby", "F. Scott Fitzgerald", 218, 9)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 417, 10)
libro3 = Libro("1984", "George Orwell", 328, 8)
libro4 = Libro()

conjunto_libros.agregar_libro(libro1)
conjunto_libros.agregar_libro(libro2)
conjunto_libros.agregar_libro(libro3)

conjunto_libros.mostrar_contenido()

conjunto_libros.eliminar_libro_por_titulo("1984")
conjunto_libros.mostrar_contenido()

conjunto_libros.mostrar_libros_mayor_calificacion()
conjunto_libros.mostrar_libros_menor_calificacion()

'''