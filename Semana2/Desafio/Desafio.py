#DECLARACION DE VARIABLES
texto=input('Ingrese un texto: \n')
letras= set()
bandera=1
contadorLetra=0
indice=-1
contadorPython=0
bandera2=0
#ASIGNACION DE LAS 3 LETRAS PARA ANALIZAR

while len(letras)<3:
        letra=input('Ingrese una letra: ')
        #Discriminar el primer valor
        if len(letra)==1 and bandera==1:
            letras.add(letra)
            bandera=0
        #discrimina la letra si es una palabra o si esta repetida
        if len(letra)==1 and (not letra in letras):
            letras.add(letra)
        else:
             print('ERROR, INGRESE UNA LETRA Y QUE NO ESTE REPETIDA')
#print(letras) ESTE PRINT FUE PARA CONFIRMAR EL GUARDADO DE 3 CARACTERES EN EL ARRAY

#-----------PUNTO 1-----------#
'''
letraConjunto: hace referencia a las letras elemento del conjunto letras
letraTexto: hace referencia a las letras de cada caracter del texto
'''
for letraConjunto in letras:
    for letraTexto in texto:
        if letraConjunto.lower()==letraTexto.lower():
            contadorLetra+=1
    else:
        print (f'La letra {letraConjunto} apareció {contadorLetra} veces.')
        contadorLetra=0
#-----------PUNTO 2-----------#
contadorPalabra=texto.split()
print(f'La cantidad de palabras escritas fue de {len(contadorPalabra)}')
#-----------PUNTO 3-----------#
print (f'La primerra letra es: {texto[0]}\nLa ultima letra es: {texto[-1]}')
#-----------PUNTO 4----------#
for i in range(len(texto)):
    print(f'{texto[indice]}',end='')
    indice-=1
else:
     print('\n')
#-----------PUNTO 5----------#
for palabra in contadorPalabra:
    if palabra.lower()=='python':
        print ('La frase incluye a la palabra \"PYTHON\"')
        bandera2=1
        break
if bandera2!=1:
    print ('La frase no incluye python')