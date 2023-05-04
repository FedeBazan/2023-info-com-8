texto = input('Ingrese un texto:\n')
letras = []

while len(letras) < 3:
    letra = input('Ingrese una letra: ')
    if len(letra) == 1 and letra not in letras:
        letras.append(letra)

for letra in letras:
    print(f'La letra {letra} apareció {texto.count(letra)} veces.')

print(f'La cantidad de palabras escritas fue de {len(texto.split())}')
print(f'La primera letra es: {texto[0]}\nLa última letra es: {texto[-1]}')
print(''.join(reversed(texto)))

if 'python' in texto.lower():
    print('La frase incluye la palabra \"PYTHON\"')
else:
    print('La frase no incluye la palabra \"PYTHON\"')