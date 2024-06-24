#EJEMPLOS DEL MUNDO REAL POO

# Ejemplo de una biblioteca que gestiona préstamos de libros

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        libro.prestar()
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        libro.devolver()
        self.libros_prestados.remove(libro)


# Ejemplo de uso del código

# Crear algunos libros
libro1 = Libro("Python Crash Course", "Eric Matthes", "9781593279288")
libro2 = Libro("Clean Code", "Robert C. Martin", "9780132350884")

# Crear un cliente
cliente1 = Cliente("Juan Pérez")

# El cliente toma prestado un libro
cliente1.tomar_prestado(libro1)

# El cliente intenta tomar prestado el mismo libro nuevamente
cliente1.tomar_prestado(libro1)

# El cliente toma prestado otro libro
cliente1.tomar_prestado(libro2)

# El cliente devuelve un libro
cliente1.devolver_libro(libro1)
# Añadir archivos al área de preparación
