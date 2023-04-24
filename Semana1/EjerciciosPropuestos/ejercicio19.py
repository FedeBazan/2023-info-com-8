'''19-Escribe un programa que solicite al usuario un número decimal y luego
imprima la parte entera y decimal por separado.'''

num=input('Ingrese un numero decimal: ')
lista=num.split("." or ",")
print(f'Parte entera: {lista[0]} \nParte decimal: {lista[1]}')
