import os

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as f:
                    for linea in f:
                        id, nombre, cantidad, precio = linea.strip().split(',')
                        self.productos[id] = {
                            'nombre': nombre,
                            'cantidad': int(cantidad),
                            'precio': float(precio)
                        }
            except FileNotFoundError:
                print("Archivo no encontrado, creando uno nuevo.")
            except Exception as e:
                print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.archivo, 'w') as f:
                for id, datos in self.productos.items():
                    f.write(f"{id},{datos['nombre']},{datos['cantidad']},{datos['precio']}\n")
        except PermissionError:
            print("Error: Permiso denegado al guardar el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, id, nombre, cantidad, precio):
        """Añade un producto al inventario y actualiza el archivo."""
        self.productos[id] = {
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio
        }
        self.guardar_inventario()
        print("Producto añadido exitosamente.")

    def actualizar_producto(self, id, nombre=None, cantidad=None, precio=None):
        """Actualiza un producto existente y guarda los cambios en el archivo."""
        if id in self.productos:
            if nombre is not None:
                self.productos[id]['nombre'] = nombre
            if cantidad is not None:
                self.productos[id]['cantidad'] = cantidad
            if precio is not None:
                self.productos[id]['precio'] = precio
            self.guardar_inventario()
            print("Producto actualizado exitosamente.")
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self, id):
        """Elimina un producto del inventario y actualiza el archivo."""
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print("Producto eliminado exitosamente.")
        else:
            print("Producto no encontrado.")

            # Crear una instancia del sistema de inventario
            inventario = Inventario()

            # Añadir un producto
            inventario.añadir_producto('001', 'Laptop', 10, 1200.50)

            # Actualizar un producto
            inventario.actualizar_producto('001', cantidad=8)

            # Eliminar un producto
            inventario.eliminar_producto('001')