'''
7-Crear un diccionario con los nombres de tres ciudades y sus respectivas
poblaciones. Agregar una cuarta ciudad al diccionario con su respectiva
población. Mostrar el diccionario resultante.
'''
ciudades={
    'Buenos Aires':2890151,
    'Cordoba':1317298,
    'Rosario':948312
}
print(ciudades)
#---Agregar una ciudad y mostrar
newCity=input('Agrega una ciudad: ')
newPoblation=int(input('Agrega su poblacion: '))
ciudades[newCity]=newPoblation
print(ciudades)