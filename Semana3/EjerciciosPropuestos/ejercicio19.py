'''19-Escribe un programa que pida al usuario un número y luego imprima si ese
número es un número perfecto o no. Un número perfecto es aquel que es igual a
la suma de sus divisores propios (excluyendo el propio número).
Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6'''

n = int(input("Ingresa un número: "))
sum_divisores = 0
# Recorremos los posibles divisores del número
for i in range(1, n):
    # Si el número es divisible por i, lo agregamos a la suma de divisores
    if n % i == 0:
        sum_divisores += i
# Comprobamos si el número es perfecto o no
if sum_divisores == n:
    print(f"{n} es un número perfecto")
else:
    print(f"{n} no es un número perfecto")