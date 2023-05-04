'''
13-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de asteriscos con esa cantidad de filas.
*
**
***
****
*****
'''
numero=int(input('Ingrese numero para armar triangulo: '))
fila=1
for i in range(numero):
    for j in range (fila):
        print('*',end='')
    fila +=1
    print('')
