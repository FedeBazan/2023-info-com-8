'''10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
una vocal o una consonante.
'''
letra=input('Escriba una letra: ')

if (ord(letra)>=65 and ord(letra)<=90) or (ord(letra)>=97 and ord(letra)<=122):
    if letra.lower()=='a' or letra.lower()=='e' or letra.lower()=='i' or letra.lower()=='o' or letra.lower()=='u':
        print(f'{letra} es una VOCAL')
    else:
        print(f'{letra} es una CONSONANTE')
else:
    print('NO es una letra')