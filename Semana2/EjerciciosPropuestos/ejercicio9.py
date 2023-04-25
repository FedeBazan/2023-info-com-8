'''9-Escribir un programa que pida al usuario tres números y muestre por pantalla
el mayor de ellos.
'''
num1=int(input('Ingrese un numero: '))
num2=int(input('Ingrese un numero: '))
num3=int(input('Ingrese un numero: '))

if num1>num2 and num1>num3:
    print(f'{num1} es el mayor')
elif num2>num1 and num2>num3:
    print(f'{num2} es el mayor')
elif num3>num1 and num3>num2:
    print(f'{num3} es el mayor')
else:
    print('No hay un numero mayor')