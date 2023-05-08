'''
12-Escribe un programa que pida al usuario una lista de números separados por
comas y calcule su promedio.

'''
numeros = input("Ingrese una lista de números separados por comas: ")
lista = [int(n) for n in numeros.split(",")]
promedio = sum(lista) / len(lista)
print(f"El promedio de los números es: {promedio}")