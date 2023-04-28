'''
Crea un programa que pida al usuario el radio de un círculo y calcule su área.
La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
Supongamos que pi = 3.1416
'''

PI=3.1416

radio=float(input('Ingrese el radio del circulo: '))
#print(f'{round(radio)}') al no poner parametro para redondear decimales el valor de radio solo tomara la parte entera
print (f'El area del circulo es : {round(PI*radio*radio,2)}')

'''
Funcoin round() 
Es una función de redondeo y se invoca de esta forma round(numero para redondear, decimales a mostrar despues de ',')

'''