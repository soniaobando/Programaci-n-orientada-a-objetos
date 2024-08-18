class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y Setters
    def get_id_producto(self):
        return self.id_producto

    def set_id_producto(self, id_producto):
        self.id_producto = id_producto

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    #3
    from producto import Producto

    class Inventario:
        def __init__(self):
            self.productos = []

        def agregar_producto(self, producto):
            if not any(p.get_id_producto() == producto.get_id_producto() for p in self.productos):
                self.productos.append(producto)
            else:
                print("Error: El ID del producto ya existe.")

        def eliminar_producto(self, id_producto):
            self.productos = [p for p in self.productos if p.get_id_producto() != id_producto]

        def actualizar_producto(self, id_producto, cantidad=None, precio=None):
            for producto in self.productos:
                if producto.get_id_producto() == id_producto:
                    if cantidad is not None:
                        producto.set_cantidad(cantidad)
                    if precio is not None:
                        producto.set_precio(precio)
                    break
            else:
                print("Producto no encontrado.")

        def buscar_producto(self, nombre):
            return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

        def mostrar_productos(self):
            for producto in self.productos:
                print(producto)

        #4
        from inventario import Inventario
        from producto import Producto

        def mostrar_menu():
            print("\nSistema de Gestión de Inventarios")
            print("1. Añadir nuevo producto")
            print("2. Eliminar producto por ID")
            print("3. Actualizar producto por ID")
            print("4. Buscar producto(s) por nombre")
            print("5. Mostrar todos los productos")
            print("6. Salir")

        def main():
            inventario = Inventario()

            while True:
                mostrar_menu()
                opcion = input("Seleccione una opción: ")

                if opcion == '1':
                    id_producto = input("Ingrese ID del producto: ")
                    nombre = input("Ingrese nombre del producto: ")
                    cantidad = int(input("Ingrese cantidad del producto: "))
                    precio = float(input("Ingrese precio del producto: "))
                    producto = Producto(id_producto, nombre, cantidad, precio)
                    inventario.agregar_producto(producto)

                elif opcion == '2':
                    id_producto = input("Ingrese ID del producto a eliminar: ")
                    inventario.eliminar_producto(id_producto)

                elif opcion == '3':
                    id_producto = input("Ingrese ID del producto a actualizar: ")
                    cantidad = input("Ingrese nueva cantidad (o presione Enter para no cambiarla): ")
                    precio = input("Ingrese nuevo precio (o presione Enter para no cambiarlo): ")
                    inventario.actualizar_producto(id_producto, cantidad=int(cantidad) if cantidad else None,
                                                   precio=float(precio) if precio else None)

                elif opcion == '4':
                    nombre = input("Ingrese nombre del producto a buscar: ")
                    resultados = inventario.buscar_producto(nombre)
                    if resultados:
                        for producto in resultados:
                            print(producto)
                    else:
                        print("No se encontraron productos con ese nombre.")

                elif opcion == '5':
                    inventario.mostrar_productos()

                elif opcion == '6':
                    print("Saliendo del sistema.")
                    break

                else:
                    print("Opción no válida. Intente de nuevo.")

        if __name__ == "__main__":
            main()