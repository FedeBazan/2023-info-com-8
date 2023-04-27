'''
8-Crear una lista con los números del 1 al 10 y mostrarlos en orden inverso.
'''
numeros=[1,2,3,4,5,6,7,8,9,10]
indice=-1
for i in numeros:
    print(numeros[indice],end=' ')
    indice-=1