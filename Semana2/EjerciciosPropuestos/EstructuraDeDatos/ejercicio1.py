'''Crear un diccionario con los nombres de tres frutas y sus respectivos precios y
mostrar el diccionario completo.
'''
verduras={'Tomate':600,'Papa':200,'Zanahoria':250}
print('Precios de Verduras por Kilo:')

for verdura,precio in verduras.items():
    print(f'Verdura:{verdura} Precio(kg.):{precio}')