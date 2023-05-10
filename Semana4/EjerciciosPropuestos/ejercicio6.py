'''
6-Crea una función llamada es_par que tome un número como parámetro y
devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
devuelva Es impar o No es par.
'''
def es_par(numero):
    print(f'{numero} es par' if numero%2==0 else f'{numero} es impar')
num=int(input('Ingrese un numero: '))
es_par(num)