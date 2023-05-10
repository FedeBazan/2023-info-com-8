'''
5-Crea una función llamada es_divisible que tome dos números enteros como
parámetros y devuelva Es divisible si el primer número es divisible por el
segundo número, o No es divisible en caso contrario.
'''
def es_divisible(num1,num2):
    return num1%num2==0
num1=int(input('Ingrese un numero: '))
num2=int(input('Ingrese un numero: '))
print(f'{num1} es divisible por {num2}' if es_divisible(num1,num2) else f'{num1} no es divisible por {num2}')