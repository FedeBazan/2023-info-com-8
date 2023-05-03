'''
6-Escribe un programa que pida al usuario una palabra y luego imprima la misma
palabra pero con las letras en orden inverso.
'''
palabra=input('Escriba una palabra: ')
indice=-1
for i in palabra:
    print(palabra[indice],end='')
    indice-=1