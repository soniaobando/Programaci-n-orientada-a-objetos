class Contacto:
    def __init__(self, nombre, telefono, email, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}, Dirección: {self.direccion}"


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def eliminar_contacto(self, nombre):
        self.contactos = [c for c in self.contactos if c.nombre != nombre]

    def consultar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
        return None

    def visualizar_agenda(self):
        return "\n".join(str(c) for c in self.contactos)


# Ejemplo de uso
agenda = Agenda()
contacto1 = Contacto("Juan Pérez", "123456789", "juan@example.com", "Calle Falsa 123")
agenda.agregar_contacto(contacto1)

print(agenda.visualizar_agenda())
