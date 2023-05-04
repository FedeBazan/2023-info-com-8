'''
17-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con las palabras en orden inverso.

'''
texto = input("Ingrese una cadena de texto: ")
palabras = texto.split() 

palabrasRevertidas = palabras[::-1]

textoRevertido = " ".join(palabrasRevertidas)

print(textoRevertido)