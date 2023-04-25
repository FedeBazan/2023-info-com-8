'''3-Escribir un programa que pida al usuario dos números y muestre por pantalla
cuál de ellos es mayor.
'''
num1=int(input('Ingrese un numero: '))
num2=int(input('Ingrese otro numero: '))

if num1>num2:
    print(f'{num1} es mayor que {num2}')
elif num1<num2:
    print(f'{num2} es mayor que {num1}')
else:
    print('Los numeros son equivalentes')