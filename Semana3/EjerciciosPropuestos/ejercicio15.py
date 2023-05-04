'''
15-Escribe un programa que pida al usuario una cadena de texto y determine
cuántas veces aparece cada letra en la cadena.'''
texto=input('Escribir Texto:\n')
letras=[]
contador=0
for letra in texto:
    if letra not in letras and letra!=' ':
        letras.append(letra)

for letra in letras:
    for caracter in texto:
        if letra==caracter:
            contador+=1
    print(f'La letra \"{letra}\" aparece {contador} veces.')
    contador=0