texto = input('Ingrese un texto:\n')
letras = []
contadorLetra = 0
contadorPalabra = texto.split()
indice = -1
bandera2 = 0

while len(letras) < 3:
    letra = input('Ingrese una letra: ')
    if len(letra) == 1 and letra not in letras:
        letras.append(letra)

for letra in letras:
    contadorLetra = texto.count(letra)
    print(f'La letra {letra} apareció {contadorLetra} veces.')

print(f'La cantidad de palabras escritas fue de {len(contadorPalabra)}')
print(f'La primera letra es: {texto[0]}\nLa última letra es: {texto[-1]}')
print(''.join(reversed(texto)))

if 'python' in texto.lower():
    print('La frase incluye la palabra \"PYTHON\"')
else:
    print('La frase no incluye la palabra \"PYTHON\"')