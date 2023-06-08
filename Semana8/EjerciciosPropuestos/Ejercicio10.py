'''
Ejercicio 10 : Tomamos un Mate

Modela una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina.
La clase debe contener como miembros:
    +Un atributo para la cantidad de cebada restantes hasta que se lava el mate (reprentada por un número).
    *Un atributo para el estado (lleno o vacío)
    *El contructor debe recibir como parámetro n, la cantidad máxima de cebadas
    en base a la cantidad de yerba vertida en el recipiente.
    *Un metodo cebar, que llena el mate con agua. Si te intenta cebar con el mate lleno,
    se debe lanzar una excepcion que imprima el mensaje ¡Cuidado!¡Te quemaste!
    *Un método beber, que vacia el mate y ke resta una cebada disponible. Si se intenta 
    beber un mate vacío, se debe lanzar una excepción que imprima el mensaje.¡El mate esta vacio!
    *Es posible seguir cebando y bebiendo el mate auqnue no haya cebadas disponibles.En ese caso la
    cantidad de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje
    de aviso:
        Advertencia: "el mate esta lavado"
    pero no se debe lanzar una excepción.
'''