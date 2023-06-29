from datetime import datetime
import random
import string

# Clase Usuario
# atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de registro, avatar, estado, online
# métodos: login(), registrar()
class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = estado
        self.online = True

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}\nID: {self.id}\nEstado: {'Conectado' if self.online else 'Desconectado'}"
    
    @staticmethod
    def generar_id():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    
    def registrar(self):
        self.id = self.generar_id()
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.telefono = input("Ingrese su teléfono: ")
        self.username = input("Ingrese su username: ")
        self.email = input("Ingrese su email: ")
        self.contraseña = input("Ingrese su contraseña: ")
        self.fecha_registro = datetime.now()
        self.avatar = input("Ingrese su avatar: ")
        self.estado = "activo"
        self.online = True
    
    def login(self, username, contraseña):
        if self.username == username and self.contraseña == contraseña:
            self.online = True
            return True
        else:
            return False

# Clase Publico(Usuario)
# atributo: es_publico
# métodos: registrar(), comentar()

class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online, es_publico):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_publico = True
    
    def registrar(self):
        super().registrar()

    @staticmethod
    def generar_id():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def login(self):
        super().usuario()

    def comentar(self):
        contenido = input("Ingrese el contenido del comentario: ")
        nuevo_comentario = Comentario(
            id=Comentario.generar_id(),
            id_articulo=articulo.id,
            id_usuario=username,
            contenido=contenido,
            fecha_hora=datetime.now(),
            estado="publicado"
        )
        
        nuevo_comentario.mostrar_comentario(nuevo_comentario.id_articulo, nuevo_comentario.id_usuario, nuevo_comentario.contenido, nuevo_comentario.fecha_hora)

# clase Colaborador(Usuario)
# atributos: es_colaborador
# métodos: registrar(), comentar(), publicar()

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online, es_colaborador):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_colaborador = es_colaborador

    def registrar(self):
        super().registrar()

    def comentar(self):
        contenido = input("Ingrese el contenido del comentario: ")
        nuevo_comentario = Comentario(
            id=Comentario.generar_id(),
            id_articulo=articulo.id,
            id_usuario=username,
            contenido=contenido,
            fecha_hora=datetime.now(),
            estado="pendiente"
        )
        nuevo_comentario.mostrar_comentario(nuevo_comentario.id_articulo, nuevo_comentario.id_usuario, nuevo_comentario.contenido, nuevo_comentario.fecha_hora)
    
    def publicar(self):
        self.titulo = input("Ingrese el título del artículo: ")
        self.contenido = input("Ingrese el contenido del artículo: ")
        self.resumen = input("Ingrese el resumen del artículo: ")

    def mostrar_articulo(self):
        print("==============================================================")
        print(f"El nuevo artículo es:")
        print(f"Artículo: {self.titulo}")
        print(f"Contenido:\n{self.contenido}")
        print(f"Resumen: {self.resumen}")
        print("==============================================================")
        

# Clase Articulo
# atributos: id, titulo, contenido, id_usuario, fecha_hora, estado
# métodos: generar_id(), mostrar_articulo(), mostrar_estado()

class Articulo:
    def __init__(self, id, titulo, contenido, id_usuario, fecha_hora, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.id_usuario = id_usuario
        self.fecha_hora = fecha_hora
        self.estado = estado

    def __str__(self):
        return f"Artículo: {self.titulo}\nID: {self.id}\nEstado: {self.mostrar_estado()}"
    
    @staticmethod
    def generar_id():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def mostrar_articulo(self):
        print(f"Artículo: {self.titulo}")
        print(f"Contenido:\n{self.contenido}")
        print(f"Autor: {self.id_usuario}")
        print(f"Fecha y Hora: {self.fecha_hora}")
        print(f"Estado: {self.mostrar_estado()}")

    def mostrar_estado(self):
        if self.estado == "pendiente":
            return "Pendiente de revisión"
        elif self.estado == "publicado":
            return "Publicado"
        else:
            return "Estado desconocido"

# Clase Comentario
# atributos: id, id_articulo, id_usuario, contenido, fecha_hora, estado
# métodos: generar_id(), mostrar_comentario()

class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido, fecha_hora, estado):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.estado = estado

    def __str__(self):
        return f"Comentario: {self.id}\nContenido: {self.contenido}\nEstado: {self.estado}"
    
    @staticmethod
    def generar_id():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def mostrar_comentario(self, id_articulo, id_usuario, contenido, fecha_hora):
        print("==============================================================")
        print(f"Comentario en el artículo {id_articulo}:")
        print(f"Usuario: {id_usuario}")
        print(f"Contenido: {contenido}")
        print(f"Fecha y Hora: {fecha_hora}")
        print("==============================================================")


#### Menu ####

username_default = "pythoneers"
password_default = "1234"
user_publico = Publico(id="", nombre="", apellido="", telefono="", username="", email="", contraseña="", fecha_registro=None, avatar="", estado="", online=False, es_publico=True)
user_colaborador = Colaborador(id="", nombre="", apellido="", telefono="", username=username_default, email="", contraseña="", fecha_registro=None, avatar="", estado="", online=False, es_colaborador=True)

articulo = Articulo(
    id=Articulo.generar_id(),
    titulo="Mi artículo de prueba",
    contenido="Este es el contenido de mi artículo de prueba.",
    id_usuario=user_colaborador.id,
    fecha_hora=datetime.now(),
    estado="pendiente"
)

tipo = input(f"¿Qué tipo de usuario es?\n1. Publico\n2. Colaborador\n")

if tipo == "1":
    print(f"Bienvenido usuario, que desea hacer?\n1. Login\n2. Registrar\n3. Comentar\n")
    opcion = input()
    if opcion == "1":
        username = input("Ingrese su username: ")
        contraseña = input("Ingrese su contraseña: ")
        while username != username_default or contraseña != password_default:
            print("Usuario o contraseña incorrectos")
            username = input("Ingrese su username: ")
            contraseña = input("Ingrese su contraseña: ")
        print(f"Desea comentar?\n1. Si\n2. No\n")
        opcion = input()
        if opcion == "1":
            user_publico.comentar()
    elif opcion == "2":
        user_publico.registrar()
    elif opcion == "3":
        username = input("Ingrese su username: ")
        user_publico.comentar()
elif tipo == "2":
    print(f"Bienvenido Colaborador, que desea hacer?\n1. Registrarse\n2. Comentar\n3. Publicar\n")
    opcion = input()
    if opcion == "1":
        user_colaborador.registrar()
    elif opcion == "2":
        username = input("Ingrese su username: ") #se puede cambiar a "ingrese su nombre o algo de eso xd"
        user_colaborador.comentar()
    elif opcion == "3":
        user_colaborador.publicar()
        user_colaborador.mostrar_articulo()
else:
    print("Opción incorrecta :()")