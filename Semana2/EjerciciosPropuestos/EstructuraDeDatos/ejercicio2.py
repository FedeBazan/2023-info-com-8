'''
2-Crear una lista con los nombres de tres ciudades y agregar una cuarta ciudad al
final de la lista.
'''

#Se crea una lista con una base de ciudades y se muestra 
ciudades=['Rosario','Ressitencia','Rawson']
for i in range(len(ciudades)):
    print(f'{ciudades[i]}',end=' ')

#Se pide al usuario sobre una nueva ciudad y se muestra lal ista con la ciudad agregada
newCity=input('\nColoca el nombre de una ciudad: ')
ciudades.append(newCity)
for i in range(len(ciudades)):
    print(f'{ciudades[i]}',end=' ')