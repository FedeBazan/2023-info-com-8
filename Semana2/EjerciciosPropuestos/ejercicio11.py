'''11-Escribir un programa que pida al usuario dos números y muestre por pantalla
la suma de ellos solo si ambos son pares.'''

num1=int(input('Escribe un numero: '))
num2=int(input('Escribe un numero: '))

if num1%2==0 and num2%2==0:
    print(f'la suma entre los numeros es {num1+num2}')