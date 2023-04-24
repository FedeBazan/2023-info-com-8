'''
15-Escribe un programa que solicite al usuario una temperatura en grados
Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.
'''
temp=round(float(input('Ingrese la temperatura en grados Celcius: ')),2)
print(f'La temperatura equivalente en grados Fahrenheit es de: {temp*1.8+32} ')