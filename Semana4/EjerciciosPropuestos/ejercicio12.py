'''
12-Crea una función llamada convertir_temperatura que tome una temperatura
en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
es: Fahrenheit = (Celsius * 9/5) + 32.'''

def convertir_temperatura(grados):
    return round(grados*(9/5)+32,2)

grados=float(input('Ingrese la cantidad de grados (Celcius): '))
print (f'El equivalente en Fahrenheit de {round(grados,2)}°C es {convertir_temperatura(grados)}°F')