'''
9-Escribe un programa que pida al usuario un número y luego imprima la
secuencia de Fibonacci correspondiente a ese número.

'''
n = int(input("Ingresa un número entero positivo: "))
fibonacci = [0, 1]
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print("Los primeros", n, "números de la serie de Fibonacci son:")
print(fibonacci[:n])