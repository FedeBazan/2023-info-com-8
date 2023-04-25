'''1-Escribir un programa que pida al usuario su edad y muestre por pantalla si es
mayor de edad (18 años o más) o no.'''
edad=int(input('Ingrese su edad: '))
print('Es mayor de edad') if edad>=18 else print('Es menor de edad')

'''
Se utilizo compuesto ternario:
EJECUTAR TRUE if (condicion) else EJECUTAR FALSE

Otro camino de resolucion:
if num>=18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')
'''