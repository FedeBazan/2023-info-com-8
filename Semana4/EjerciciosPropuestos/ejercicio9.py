'''
9-Crea una función llamada promedio que tome una lista de números como
parámetro y devuelva el promedio de esos números.'''
def promedio(lista_numero):
    if len(lista_numero) == 0:
        return 0  # la lista está vacía, devolver 0
    else:
        return sum(lista_numero) / len(lista_numero)  # calcular el promedio / sum()devuelve la suma total de todos los elementos si estos son numeros

lista = []
while True:
    numero = input('Ingresa numero (o presiona enter para terminar): ')
    if not numero:  # si el usuario presiona enter sin ingresar un número, salir del bucle
        break
    lista.append(int(numero))
if len(lista) == 0:
    print('Debes ingresar al menos un número para calcular el promedio.')
else:
    print(f'El promedio de los numeros es: {promedio(lista)}')
