'''
3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
multiplicar correspondiente a ese número del 1 al 10.
'''
numero=int(input('Ingrese el numero para mostrar su tabla del 1 al 10: '))
for i in range(1,11):
    print(f'{numero}x{i}={numero*i}')