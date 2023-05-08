'''
13-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de asteriscos con esa cantidad de filas.
*
**
***
****
*****
'''
n = int(input('Ingrese el número de filas: '))
for i in range(1, n+1):
    print('*' * i)