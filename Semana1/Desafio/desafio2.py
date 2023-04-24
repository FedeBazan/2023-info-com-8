'''Escribe un programa que solicite al usuario su información personal, incluyendo
su nombre completo, edad, estatura, peso, dirección y número de teléfono.
A continuación, el programa deberá imprimir un mensaje con los datos
ingresados por el usuario en el siguiente formato:
La información ingresada es la siguiente:
Nombre completo: [nombre completo]
Edad: [edad]
Estatura: [estatura] cm
Peso: [peso] kg
Dirección: [dirección]
Número de teléfono: [número de teléfono]'''

nombre=input('Ingrese nombre completo: ')
edad=int(input('Ingrese edad: '))
estatura=int(input('Ingerese estatura en cm: '))
peso=round(float(input('Ingrese peso en Kg: ')),2)
direccion=input('Ingrese direccion: ')
numero=input('Ingrese numero de telefono/celular: ')

print(f'''---REGISTRO DE DATOS---
Nombre:{nombre}
Edad:{edad}
Estatura:{estatura} Cm.
Peso:{peso} Kg.
Direccion:{direccion}
Numero:{numero}
---------------------------------
''')