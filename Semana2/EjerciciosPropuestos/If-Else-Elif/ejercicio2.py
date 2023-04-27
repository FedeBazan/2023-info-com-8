'''2-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es positivo, negativo o cero.'''
num=int(input('Escribe un numero entero: '))
if num>0:
    print('Es un numero positivo')
elif num<0:
    print('Es un numero negativo')
else:
    print('Es el numero 0(cero)')