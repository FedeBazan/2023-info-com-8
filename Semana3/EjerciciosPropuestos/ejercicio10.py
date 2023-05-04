'''
10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con todas las vocales en mayúscula.

'''
texto=input('Ingrese un texto: ')
vocales=['a','e','i','o','u']
indice=0

for letra in texto:
    print(texto[indice].upper(),end='') if (letra in vocales) else print(texto[indice],end='')
    indice+=1