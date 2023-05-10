'''1-Crea una función llamada suma que tome dos números como parámetros y
devuelva la suma de ellos.'''
def suma(num1,num2):
    return num1+num2
num1=int(input('Ingrese un numero: '))
num2=int(input('Ingrese un numero: '))
print(f'La suma entre {num1} y {num2} es {suma(num1,num2)}')