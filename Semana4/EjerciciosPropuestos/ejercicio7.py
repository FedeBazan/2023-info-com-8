'''
7-Crea una función llamada imprimir_pares que tome un número entero como
parámetro y imprima todos los números pares desde 1 hasta ese número.
'''
def imprimir_pares(numero):
    print(f'Numeros pares entre 1 y {numero}:', end=' ')
    for i in range(2, numero+1, 2):
        print(i, end=' ')
    print()  # Salto de línea después de imprimir los números

numero=int(input('Ingrese numero: '))
imprimir_pares(numero)