'''
7-Escribe un programa que pida al usuario una palabra y determine si es un
palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
izquierda).'''
palabra=input('Escribe una palabra: ')
indice=-1
palabra2=''
for i in palabra:
    palabra2+=palabra[indice]
    indice-=1
if palabra2==palabra:
    print(f'{palabra} es Palíndromo')
else:
    print(f'{palabra} no es Palíndromo')