'''
13-Crear una lista con los nombres de tres colores y agregar dos colores más al
final de la lista. Mostrar la lista resultante.

'''

colores=[]
for i in range(3):
    color=input('Ingresa nombre del color: ')
    colores.append(color)
else:
    print('Lista de los colores:')
    for color in colores:
        print (color)
    for i in range(2):
        color=input('Agregar un color mas: ')
        colores.append(color)
    print('Lista de colores agregando los 2 ultimos colores:')
    for color in colores:
        print (color)