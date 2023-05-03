'''
8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
el número de palabras que contiene.'''
texto=input('escriba un texto:\n')
contadorPalabras=texto.split()
print(f'El número total de palabras es {len(contadorPalabras)}')