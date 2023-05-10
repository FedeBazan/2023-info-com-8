'''8-Crea una función llamada es_palindromo que tome una cadena de texto como
parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso
contrario.
'''
def es_palindromo(texto):
    if ' ' in texto:
        print('Advertencnia, hay un espacio en el dato pedido')
        return False  # hay más de una palabra en la cadena
    else:
        return texto == texto[::-1]  # verificar si es palíndromo

texto = input('Ingrese una sola palabra: ')
print(f'\"{texto}\" es palindromo' if es_palindromo(texto) else f'\"{texto}\" no es palindromo')
