'''
11-Crea una función llamada contar_vocales que tome una cadena de texto como
parámetro y devuelva el número de vocales que contiene.'''

import re

def contar_vocales(texto):
    if not isinstance(texto, str):
        print("El parámetro debe ser una cadena de texto.")
        return 0
    texto_limpio = texto.lower()  # convertir todo a minúsculas
    patron = re.compile(r'[aeiouáéíóú]')  # expresión regular para buscar vocales, otra variante del count con la libreria re
    vocales = re.findall(patron, texto_limpio)# busca todas las coincidencias guardadas en la variable 'patron' en 'texto limpio'
    return len(vocales)

texto=input('Ingrese texto:\n')
print(f'La cantidad de vocales en el texto es de {contar_vocales(texto)}')