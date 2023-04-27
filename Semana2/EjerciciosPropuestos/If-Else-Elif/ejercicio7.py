'''7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
es una letra mayúscula, una letra minúscula, un número o un carácter especial.
'''
char=input('Escribe un caracter: ')
carac=ord(char)
if carac>=48 and carac<=57:
    print(f'{char} es un numero')
elif carac>=97 and carac<=122:
    print (f'{char} es una minuscula')
elif carac>=65 and carac<=90:
    print (f'{char} es una mayusucula')
else:
    print (f'{char} es un caracter especial')

#NOTA: Se puede mejorar en caso de que el user coloque mas de un caracter devolver un mensaje de error

'''
Hay varias formas de resolucion, en esta se utiliza el coddigo ASCII
la funcion ord() devuelve el numero dominal que representa el caracter.
https://elcodigoascii.com.ar
por otro lado la funcion chr() toma el valor numerico y muestra el caracter
que representa, si este existe.
'''