'''
5-Escribe un programa que imprima la suma de todos los números pares del 1 al
100.

'''
sum = 0
for i in range(2, 101, 2):
    sum += i
print(f"La suma de los números pares del 1 al 100 es: {sum}")
