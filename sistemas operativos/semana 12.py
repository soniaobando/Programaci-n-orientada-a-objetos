# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.detalles = (titulo, autor)  # Tupla que almacena título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.detalles[0]} por {self.detalles[1]} (ISBN: {self.isbn}, Categoría: {self.categoria})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para los libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        if self.libros_prestados:
            print(f"Libros prestados a {self.nombre}:")
            for libro in self.libros_prestados:
                print(f"- {libro}")
        else:
            print(f"{self.nombre} no tiene libros prestados.")

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
        self.ids_usuarios = set()  # Conjunto para asegurar IDs únicos de usuarios

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro_removido = self.libros.pop(isbn)
            print(f"Libro removido: {libro_removido}")
        else:
            print(f"No se encontró ningún libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")
        else:
            print(f"El ID {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario_removido = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario dado de baja: {usuario_removido}")
        else:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("Error: Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.devolver_libro(libro)
            print(f"Libro devuelto: {libro} por {usuario.nombre}")
        else:
            print("Error: Usuario o libro no encontrado.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        if criterio == "titulo":
            resultados = [libro for libro in self.libros.values() if libro.detalles[0].lower() == valor.lower()]
        elif criterio == "autor":
            resultados = [libro for libro in self.libros.values() if libro.detalles[1].lower() == valor.lower()]
        elif criterio == "categoria":
            resultados = [libro for libro in self.libros.values() if libro.categoria.lower() == valor.lower()]

        if resultados:
            print(f"Resultados de búsqueda por {criterio} '{valor}':")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros para el {criterio} '{valor}'.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            usuario.listar_libros_prestados()
        else:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")


# Prueba del sistema
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "12345")
libro2 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "67890")

# Añadir libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Crear usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("Ana Gómez", "002")

# Registrar usuarios en la biblioteca
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("001", "12345")

# Listar libros prestados
biblioteca.listar_libros_prestados("001")

# Devolver libro
biblioteca.devolver_libro("001", "12345")

# Buscar libro por título
biblioteca.buscar_libro("titulo", "El Quijote")
