'''
10-Crea una función llamada calcular_factorial que tome un número entero como
parámetro y devuelva el factorial de ese número. El factorial de un número
entero positivo n se define como el producto de todos los números enteros
positivos desde 1 hasta n.'''

def calcular_factorial(numero):
    fac=1
    for i in range(1,numero+1):
        fac*=i
    return fac
numero=int(input('Coloque un numero para obtener el factorial del mismo: '))
print(f'El factorial de \"{numero}\" es \"{calcular_factorial(numero)}\"')