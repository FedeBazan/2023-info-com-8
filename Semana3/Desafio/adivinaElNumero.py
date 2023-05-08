#Autor: Bazan Julio Pablo Federico
#12:55 8/5/2023

import random

nombre = input("Bienvenido! ¿Cuál es tu nombre? ")
print(f"Bienvenido, {nombre}! Estoy pensando en un número entre 1 y 100. Tienes 8 intentos para adivinarlo.")

numero = random.randint(1, 100)
intentos_maximos = 8
intentos_realizados = 0

while intentos_realizados < intentos_maximos:
    print('----------------------')
    intentos_restantes = intentos_maximos - intentos_realizados
    print(f"Intento #{intentos_realizados + 1} de {intentos_maximos}. Te quedan {intentos_restantes} intentos.")
    numero_ingresado = input("Ingresa un número entre 1 y 100: ")
        
    if not numero_ingresado.isdigit():
        print("Lo siento, eso no es un número entero válido. Por favor intenta de nuevo.")
        intentos_realizados += 1
        continue
        
    numero_ingresado = int(numero_ingresado)
        
    if numero_ingresado == numero:
        print(f"---------\nFelicitaciones, {nombre}! Adivinaste el número en el intento #{intentos_realizados + 1}!---------\n")
        break
    
    if numero_ingresado < numero:
        print(f"El número que estoy pensando es mayor que {numero_ingresado}.")
    else:
        print(f"El número que estoy pensando es menor que {numero_ingresado}.")
        
    intentos_realizados += 1
    
if intentos_realizados == intentos_maximos:
    print(f"Lo siento, {nombre}. No adivinaste el número en los {intentos_maximos} intentos disponibles. El número que estaba pensando era: {numero}")
