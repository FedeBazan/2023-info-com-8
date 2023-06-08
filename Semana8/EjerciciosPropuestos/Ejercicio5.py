'''
Ejercicio 5: Gestion de Donaciones

Nos piden que diseñemos un programa para gestionar donaciones de alimentos.
Los productos tienen los siguientes atributos:
    *Nombre
    *Cantidad
Tenemos dos tipos de productos:
    *Perecedero: tiene un atributo llamado días a caducar.
    *No perecedero: tiene un atributo llamado tipo.
Tendremos una funcion llamada Calcular, que segun cada clase hara una cosa u otra
otra, a esta funcion se le envia la cantidad por producto y entidades a las cuales
se entregaran donaciones.
    *Debe obtener la cantidad que se enviara a cada enidad, sabiendo que la distri
    bucion debe ser lo mas equitativa posible.En caso que sobren productos, se almacenan
    para el próximo ciclo de donación
    +Además si el producto es perecedero, se informará:
        +Si le queda menos de 10 días para caducar, la entrega debe hacerse en el 
        día actual
        +Si le queda 1 mes para caducar, la entrega debe hacerse en el ploazo de 1 semana.
    +Si fuera No Perecedero, se informa cuántos productos se entregarán por entidad
    y que queda libre la elección de la fecha de entrega siempre que no supere el mes.
'''
