'''4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
pantalla si está aprobado (5 o más) o no.'''

nota=int(input('Ingrese la nota del alumno: '))
print('El alumno APROBO') if nota>=5 else print('El alumno DESAPROBO')