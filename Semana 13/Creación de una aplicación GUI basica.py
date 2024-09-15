import tkinter as tk
from tkinter import ttk

# Función para agregar información a la lista
def agregar_info():
    info = entry.get()
    if info:
        listbox.insert(tk.END, info)
        entry.delete(0, tk.END)

# Función para limpiar la lista
def limpiar_info():
    listbox.delete(0, tk.END)
    entry.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Crear y colocar los componentes
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack(pady=5)

entry = tk.Entry(ventana, width=50)
entry.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_info)
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_info)
boton_limpiar.pack(pady=5)

listbox = tk.Listbox(ventana, width=50, height=10)
listbox.pack(pady=5)

# Ejecutar el bucle principal
ventana.mainloop()
import tkinter as tk
from tkinter import ttk

# Función para agregar información a la lista
def agregar_info():
    info = entry.get()  # Obtener el texto ingresado
    if info:  # Verificar que no esté vacío
        listbox.insert(tk.END, info)  # Insertar el texto en la lista
        entry.delete(0, tk.END)  # Limpiar el campo de texto

# Función para limpiar la lista y el campo de texto
def limpiar_info():
    listbox.delete(0, tk.END)  # Eliminar todos los elementos de la lista
    entry.delete(0, tk.END)  # Limpiar el campo de texto

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Crear y colocar los componentes
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack(pady=5)

entry = tk.Entry(ventana, width=50)
entry.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_info)
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_info)
boton_limpiar.pack(pady=5)

listbox = tk.Listbox(ventana, width=50, height=10)
listbox.pack(pady=5)

# Ejecutar el bucle principal
ventana.mainloop()
