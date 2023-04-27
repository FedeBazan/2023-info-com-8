'''
10-Crear una lista con los nombres de tres frutas y eliminar la segunda fruta de la
lista. Mostrar la lista resultante.
'''
frutas=[]
for i in range(3):
    fruta=input('Ingresa nombre de la fruta: ')
    frutas.append(fruta)
else:
    print('Lista de las frutas:')
    for fruta in frutas:
        print (fruta)
    print('Lista de fruta eliminando la segunda:')
    frutas.remove(frutas[1])
    for fruta in frutas:
        print (fruta)
