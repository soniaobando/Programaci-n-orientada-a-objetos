# Clase ejemplo que utiliza constructores y destructores

class Recurso:
    def __init__(self, nombre):
        self.nombre = nombre




# Aquí podrías realizar inicializaciones adicionales según necesites


def operacion(self):
    print(f"Realizando operación con el recurso: {self.nombre}")


# Aquí irían las operaciones que realiza este recurso


def __del__(self):
    print(f"Liberando recurso: {self.nombre}")


# Aquí realizarías la limpieza o cierre de recursos
# Por ejemplo, cerrar archivos, conexiones a bases de datos, etc.

# Ejemplo de uso de la clase Recurso
