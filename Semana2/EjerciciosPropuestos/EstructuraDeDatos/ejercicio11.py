'''
11-Crear una lista con los nombres de tres animales y agregar una cuarta animal
al principio de la lista. Mostrar la lista resultante.

'''
animales=[]
for i in range(3):
    animal=input('Ingresa nombre del animal: ')
    animales.append(animal)
else:
    print('Lista de los animales:')
    for animal in animales:
        print (animal)
    animal=input('Agregar un animal mas: ')
    animales.insert(0,animal)
    print('Lista de animales agregando el ultimo animal al primero puesto:')
    for animal in animales:
        print (animal)
