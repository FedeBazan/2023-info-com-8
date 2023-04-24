'''
12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
dd/mm/aaaa y luego imprima su edad en años.
Utiliza la función .split()
'''

fecha=input('Ingrese la fecha ACTUAL en formato DD/MM/AAAA: ')
nacimiento=input('Ingrese la fecha de NACIMIENTO en formato DD/MM/AAAAA: ')

lista1=fecha.split("/")
lista2=nacimiento.split("/")

print(f'La edad aprox. es de: {int(lista1[2])-int(lista2[2])}')

#NOTA: Se puede ser mas elaborado, el código es muy minimalista