'''
16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
e imprima su índice de masa corporal (IMC).
La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).
'''

altura=round(float(input('Ingrese la altura (en mts): ')),2)
peso=round(float(input('Ingrese su peso (en kg): ')),2)
print(f'Su IMC es de {round(peso/(altura**2),2)}')