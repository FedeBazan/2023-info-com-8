'''
Ejercicio 3: Triángulo
Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los atributos, imprimir el
valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero,
isósceles o escaleno).

'''
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def obtener_lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    def obtener_tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"


# Función para verificar si un valor puede ser convertido a float
def es_float(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


# Función para validar que los lados del triángulo sean números válidos
def validar_lados(lados):
    for lado in lados:
        if not es_float(lado) or float(lado) <= 0:
            return False
    return True

# Función para obtener los lados del triángulo del usuario
def ingresar_lados():
    lados_validos = False
    while not lados_validos:
        lado1 = input("Ingrese la longitud del primer lado: ")
        lado2 = input("Ingrese la longitud del segundo lado: ")
        lado3 = input("Ingrese la longitud del tercer lado: ")

        lados = [lado1, lado2, lado3]
        lados_validos = validar_lados(lados)

        if not lados_validos:
            print("Los lados deben ser números válidos y mayores a cero. Intente nuevamente.")

    return float(lado1), float(lado2), float(lado3)


lado1, lado2, lado3 = ingresar_lados()

triangulo = Triangulo(lado1, lado2, lado3)
lado_mayor = triangulo.obtener_lado_mayor()
tipo_triangulo = triangulo.obtener_tipo_triangulo()

print("El lado con mayor longitud es:", lado_mayor)
print("El triángulo es de tipo:", tipo_triangulo)
