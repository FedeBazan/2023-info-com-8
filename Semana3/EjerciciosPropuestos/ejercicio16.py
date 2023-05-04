'''
16-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con cada palabra al revés.
'''
texto = input("Ingrese una cadena de texto: ")
palabras = texto.split() # Dividir la cadena de texto en una lista de palabras

# Recorrer cada palabra de la lista y revertirla
for i in range(len(palabras)):
    palabras[i] = palabras[i][::-1]

# Unir las palabras revertidas en una cadena de texto
textoRevertido = " ".join(palabras)

print(textoRevertido)