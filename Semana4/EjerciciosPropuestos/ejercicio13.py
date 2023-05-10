''''
13-Crea una función llamada calcular_descuento que tome dos parámetros:
precio y porcentaje_descuento. La función debe calcular y devolver el precio
después de aplicar el descuento.
'''
def importe_descuento(importe,descuento):
    return importe*(descuento/100)

def calcular_descuento(importe,descuento):
    return importe-importe_descuento(importe,descuento)

precio=float(input('Ingrese precio del producto: '))
descuento=float(input('Ingrese el descuento en %: '))
print(f'''El precio del producto es {round(precio,2)}
El descuento del {descuento}% aplica un total de descuento de ${importe_descuento(precio,descuento)}
El total a pagar es de ${calcular_descuento(precio,descuento)}''')