class Student:
    def __init__(self, cedula, nombre, apellido, correo, nota):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.nota = nota
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, cedula, nombre, apellido, correo, nota):
        new_student = Student(cedula, nombre, apellido, correo, nota)
        if nota >= 6:  # Aprobado
            new_student.next = self.head
            self.head = new_student
        else:  # Reprobado
            if not self.head:
                self.head = new_student
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_student

    def search_student(self, cedula):
        current = self.head
        while current:
            if current.cedula == cedula:
                return vars(current)
            current = current.next
        return "Estudiante no encontrado."

    def delete_student(self, cedula):
        current = self.head
        prev = None
        while current:
            if current.cedula == cedula:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return "Estudiante eliminado."
            prev = current
            current = current.next
        return "Estudiante no encontrado."

    def count_approved(self):
        current = self.head
        count = 0
        while current:
            if current.nota >= 6:
                count += 1
            current = current.next
        return count

    def count_failed(self):
        current = self.head
        count = 0
        while current:
            if current.nota < 6:
                count += 1
            current = current.next
        return count
