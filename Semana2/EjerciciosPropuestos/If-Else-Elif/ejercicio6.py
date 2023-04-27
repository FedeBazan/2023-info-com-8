'''6-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es múltiplo de 2 y de 3 a la vez.
'''
num=int(input('Escribe un numero: '))
print(f'{num} es multiplo de 2 y 3') if (num%2==0 and num%3==0) else print(f'{num} no es multiplo de 2 y 3')