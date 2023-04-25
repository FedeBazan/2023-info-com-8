'''8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
por pantalla si contiene la letra "a".'''

frase=input('Ingrese una frase: ')

for i in range(len(frase)):
    if frase[i]=='a' or frase[i]=='A':
        print ('Contiene la letra "a"')
        break
