'''
12-Escribe un programa que pida al usuario una lista de números separados por
comas y calcule su promedio.

'''
lista=[]
bandera=1
suma=0
while bandera==1:
    num=int(input('ingrese un numero:'))
    lista.append(num)
    opc=input('¿Desea agregar otro numero? (SI/NO)')
    if opc.lower()=='no':
        bandera=0
for numero in lista:
    suma+=numero
print(lista)
print(f'Promedio de numero de lista: {round(suma/len(lista),2)}')