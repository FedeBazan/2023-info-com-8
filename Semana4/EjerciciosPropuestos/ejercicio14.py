'''
14-Crea una función llamada encontrar_maximo que tome una lista de números
como parámetro y devuelva el número máximo de la lista.'''

def encontrar_maximo(lista):
    return max(lista)

# Pedir al usuario que ingrese los valores separados por comas y convertirlos a una lista
lista_numeros = [int(x) for x in input("Ingresa los números separados por comas: ").split(",")]

# Mostrar el valor máximo de la lista
print(f'El valor máximo de la lista es: {encontrar_maximo(lista_numeros)}')
