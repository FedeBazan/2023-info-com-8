'''
15-Crea una función llamada contar_palabras que tome una cadena de texto
como parámetro y devuelva el número de palabras que contiene. Se considera
que las palabras están separadas por espacios.'''

def contar_palabras(texto):
    return len(texto.split())

texto=input('Escriba un texto:\n')
print(f'El texto contiene {contar_palabras(texto)} palabras.')