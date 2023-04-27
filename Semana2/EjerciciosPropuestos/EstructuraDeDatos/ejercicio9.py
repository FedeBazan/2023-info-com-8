'''
9-Crear una lista con los nombres de tres países y ordenar la lista en orden
alfabético. Mostrar la lista resultante.

Agregado PLUS
pedir los nombres de 3 paises al usuario y mostrar la lista ordenada
'''
paises=[]
for i in range(3):
    pais=input('Ingresa nombre del Pais: ')
    paises.append(pais)
print('Lista desordenanada:',end=' ')
for pais in paises:
    print(pais,end=' ')
paises.sort()
print('\nLista ordenada:',end=' ')
for pais in paises:
    print(pais,end=' ')