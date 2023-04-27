'''
12-Crear una lista con los nombres de tres países y reemplazar el segundo país de
la lista por otro país. Mostrar la lista resultante.
'''
paises=[]
for i in range(3):
    pais=input('Ingresa nombre del pais: ')
    paises.append(pais)
else:
    print('Lista de los paises:')
    for pais in paises:
        print (pais)
    paises[1]=input('Reemplazar el segundo pais con: ')
    print('Lista de paises reemplazando el segundo pais con el ultimo agregado:')
    for pais in paises:
        print (pais)