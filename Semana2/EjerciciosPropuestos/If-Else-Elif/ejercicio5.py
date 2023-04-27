'''5-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es par o impar.
'''

num=int(input('Escribe un numero: '))
print(f'{num} es PAR') if num%2==0 else print(f'{num} es IMPAR')