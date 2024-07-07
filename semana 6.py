
class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulación: atributo privado

    def get_nombre(self):
        return self.__nombre

    def hacer_sonido(self):
        pass

# Clase derivada que muestra herencia y polimorfismo
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        return "Miau!"

# Creación de instancias y demostración de polimorfismo
def main():
    perro1 = Perro("toby")
    gato1 = Gato("manchitas")

    print(f"{perro1.get_nombre()} dice: {perro1.hacer_sonido()}")
    print(f"{gato1.get_nombre()} dice: {gato1.hacer_sonido()}")

if __name__ == "__main__":
    main()