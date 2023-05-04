'''
14-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de números como el siguiente:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
numero=int(input('Ingrese numero para armar triangulo: '))
fila=1
for i in range(numero):
    for j in range (fila):
        print(f'{fila}',end='')
    fila +=1
    print('')
