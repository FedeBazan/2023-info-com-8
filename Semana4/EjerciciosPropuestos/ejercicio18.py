'''
18-Crea una función llamada calcular_mayor_diferencia que tome una lista de
números como parámetro y devuelva la mayor diferencia entre el numero mas
alto y el numero mas bajo en la lista.
'''

def calcular_mayor_diferencia(lista):
    return max(lista) - min(lista)

lista_numeros = [int(x) for x in input("Ingresa los números separados por comas: ").split(",")]
print(f'La mayor diferencia entre {max(lista_numeros)} y {min(lista_numeros)} es: {calcular_mayor_diferencia(lista_numeros)}')
