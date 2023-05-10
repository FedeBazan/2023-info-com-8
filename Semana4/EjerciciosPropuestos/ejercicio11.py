'''
11-Crea una función llamada contar_vocales que tome una cadena de texto como
parámetro y devuelva el número de vocales que contiene.'''

def contar_vocales(texto):
    texto_minuscula=texto.lower()
    return texto_minuscula.count('a')+texto_minuscula.count('e')+texto_minuscula.count('i')+texto_minuscula.count('o')+texto_minuscula.count('u')

texto=input('Ingrese texto:\n')
print(f'La cantidad de vocales en el texto es de {contar_vocales(texto)}')