class Vehicle:
    def __init__(self, placa, marca, modelo, anio, precio):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
        self.next = None

class ParkingLot:
    def __init__(self):
        self.head = None

    def add_vehicle(self, placa, marca, modelo, anio, precio):
        new_vehicle = Vehicle(placa, marca, modelo, anio, precio)
        new_vehicle.next = self.head
        self.head = new_vehicle

    def search_vehicle(self, placa):
        current = self.head
        while current:
            if current.placa == placa:
                return vars(current)
            current = current.next
        return "Vehículo no encontrado."

    def view_vehicles_by_year(self, year):
        current = self.head
        vehicles = []
        while current:
            if current.anio == year:
                vehicles.append(vars(current))
            current = current.next
        return vehicles

    def view_all_vehicles(self):
        current = self.head
        vehicles = []
        while current:
            vehicles.append(vars(current))
            current = current.next
        return vehicles

    def delete_vehicle(self, placa):
        current = self.head
        prev = None
        while current:
            if current.placa == placa:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return "Vehículo eliminado."
            prev = current
            current = current.next
        return "Vehículo no encontrado."
