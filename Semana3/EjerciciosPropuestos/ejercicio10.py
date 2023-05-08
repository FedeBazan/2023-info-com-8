'''
10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con todas las vocales en mayúscula.

'''
texto = input('Ingrese un texto: ')
vocales = ['a', 'e', 'i', 'o', 'u']
texto_modificado = ''

for letra in texto:
    texto_modificado += letra.upper() if letra in vocales else letra

print(texto_modificado)