'''
17-Escribe un programa que solicite al usuario dos palabras y luego las imprima
en orden inverso.
Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir
"mundo hola".
Importante!!! Utiliza un solo print() 😈.
'''
frase=input('Coloque una frase: ')
fraseCadena=frase.split(" ")
indice=0
#print(fraseCadena)
for i in range(len(fraseCadena)):
    indice+=1
    print (f"{fraseCadena[indice*(-1)]}",end=" ")