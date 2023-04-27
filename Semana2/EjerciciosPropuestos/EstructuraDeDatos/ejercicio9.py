'''
9-Crear una lista con los nombres de tres países y ordenar la lista en orden
alfabético. Mostrar la lista resultante.

Agregado PLUS
pedir los nombres de 3 paises al usuario y mostrar la lista ordenada
'''
paises=[]
for i in range(3):
    pais=capitalize(input('Ingresa nombre del Pais: '))
    #capitalize(): esta funcion permite Trnsformar la primera letra en MAYUS
    paises.append(pais)
for pais in paises