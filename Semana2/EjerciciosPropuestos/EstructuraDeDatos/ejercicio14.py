'''
14-Crear una tupla con los números del 1 al 5 y mostrar la suma de todos los
elementos de la tupla
'''
tupla=(1,2,3,4,5)
suma=0
for numero in tupla:
    suma += numero
print(f'La suma total es de {suma}')