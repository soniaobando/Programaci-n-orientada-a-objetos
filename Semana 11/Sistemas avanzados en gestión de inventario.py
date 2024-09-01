
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() not in self.productos:
            self.productos[producto.get_id()] = producto
        else:
            print("Producto con este ID ya existe.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id].set_precio(precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        for producto in encontrados:
            print(producto)
        if not encontrados:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id: vars(producto) for id, producto in self.productos.items()}, f, indent=4)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                productos = json.load(f)
                self.productos = {id: Producto(**datos) for id, datos in productos.items()}
        except FileNotFoundError:
            print("Archivo no encontrado.")

def menu():
    inv = Inventario()
    while True:
        print("\nMenú de Inventario:")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Todos los Productos")
        print("6. Guardar Inventario")
        print("7. Cargar Inventario")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("Ingrese ID: ")
            nombre = input("Ingrese Nombre: ")
            cantidad = int(input("Ingrese Cantidad: "))
            precio = float(input("Ingrese Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inv.agregar_producto(producto)

        elif opcion == '2':
            id = input("Ingrese ID del producto a eliminar: ")
            inv.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva Cantidad (dejar en blanco si no desea cambiar): ")
            precio = input("Ingrese nuevo Precio (dejar en blanco si no desea cambiar): ")
            inv.actualizar_producto(id, cantidad=int(cantidad) if cantidad else None, precio=float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            inv.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inv.mostrar_productos()

        elif opcion == '6':
            archivo = input("Ingrese nombre del archivo para guardar el inventario: ")
            inv.guardar_inventario(archivo)

        elif opcion == '7':
            archivo = input("Ingrese nombre del archivo para cargar el inventario: ")
            inv.cargar_inventario(archivo)

        elif opcion == '8':
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()