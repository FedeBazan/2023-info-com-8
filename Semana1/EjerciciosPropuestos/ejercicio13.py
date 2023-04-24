'''
13-Escribe un programa que solicite al usuario su nombre y su edad, y luego
imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.

'''
nombre=input('¿Cómo se llama? ')
edad=int(input(f'Hola {nombre} Ingrese su edad: '))
print(f'{nombre}, en 10 años tendras {edad+10}')