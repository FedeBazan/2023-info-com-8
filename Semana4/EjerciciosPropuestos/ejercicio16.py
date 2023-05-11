'''
16-Crea una función llamada eliminar_duplicados que tome una lista como
parámetro y devuelva una nueva lista sin duplicados, conservando el orden
original.
'''

def eliminar_duplicados (lista):
    sin_duplicados=set()
    for numero in lista:
        sin_duplicados.add(numero)
    return list(sin_duplicados)

lista_numeros = [int(x) for x in input("Ingresa los números separados por comas: ").split(",")]
lista_sinduplicados=eliminar_duplicados(lista_numeros)
print(f'''Lista ingresada: {lista_numeros}
Lista sin duplicados: {lista_sinduplicados}
''')