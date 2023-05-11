'''
17-Crea una función llamada es_anagrama que tome dos cadenas de texto como
parámetros y devuelva True si son anagramas (es decir, si tienen las mismas
letras pero en distinto orden), o False en caso contrario.
'''

def es_anagrama(palabra1, palabra2):
    if ' ' in palabra1 or ' ' in palabra2:
        return 'ERROR: UNA DE LAS PALABRAS TIENE ESPACIO O ES UN TEXTO'
    if sorted(palabra1.lower()) == sorted(palabra2.lower()):
        return f'{palabra1} y {palabra2} son anagramas'
    else:
        return f'{palabra1} y {palabra2} no son anagramas'

    
palabra1=input('ingrese una palabra: ')
palabra2=input('ingrese otra palabra: ')
print(es_anagrama(palabra1,palabra2))