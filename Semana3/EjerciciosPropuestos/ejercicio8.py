'''
8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
el número de palabras que contiene.'''
texto = input('Escribe un texto:\n')
contador_palabras = 0
for palabra in texto.split():
    if palabra.isalpha(): #isalpha() verifica si la cadena de caracteres solo contiene letras, devuelve TRUE o FALSE
        contador_palabras += 1
print(f'El número total de palabras es {contador_palabras}')