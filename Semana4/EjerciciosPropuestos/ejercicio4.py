'''
4-Crea una función llamada es_capicua que tome un número como parámetro y
devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
derecha a izquierda) y False en caso contrario.'''
def es_capicua(numero):
    return str(numero) == str(numero)[::-1]


num = input('Ingrese un número: ')
print(f'{num} es capicua' if es_capicua(num) else f'{num} no es capicua')