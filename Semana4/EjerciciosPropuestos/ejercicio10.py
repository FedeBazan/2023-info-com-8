'''
10-Crea una función llamada calcular_factorial que tome un número entero como
parámetro y devuelva el factorial de ese número. El factorial de un número
entero positivo n se define como el producto de todos los números enteros
positivos desde 1 hasta n.'''

def calcular_factorial(numero):
    if numero < 0:
        return None # si el número es negativo, devolver None
    fac=1
    for i in range(1,numero+1):
        fac*=i
    return fac

numero=int(input('Coloque un numero para obtener el factorial del mismo: '))
factorial = calcular_factorial(numero)
if factorial is None:
    print('El número ingresado es negativo. No se puede calcular el factorial.')
else:
    print(f'El factorial de \"{numero}\" es \"{factorial}\"')
