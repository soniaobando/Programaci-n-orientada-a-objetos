import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Función para agregar un nuevo evento a la lista
def agregar_evento():
    fecha = date_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    if fecha and hora and descripcion:
        tree.insert('', 'end', values=(fecha, hora, descripcion))
        limpiar_campos()
    else:
        messagebox.showwarning("Campos vacíos", "Todos los campos deben estar llenos")

# Función para eliminar el evento seleccionado
def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        confirmacion = messagebox.askyesno("Confirmación", "¿Seguro que deseas eliminar este evento?")
        if confirmacion:
            tree.delete(seleccionado)
    else:
        messagebox.showwarning("Seleccionar evento", "Debes seleccionar un evento para eliminar.")

# Función para limpiar los campos de entrada
def limpiar_campos():
    date_entry.set_date('')
    hora_entry.delete(0, tk.END)
    descripcion_entry.delete(0, tk.END)

# Función para salir de la aplicación
def salir():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Eventos")
ventana.geometry("500x400")

# Crear el Frame principal
frame = tk.Frame(ventana)
frame.pack(pady=20)

# Lista (TreeView) para mostrar los eventos
columns = ('Fecha', 'Hora', 'Descripción')
tree = ttk.Treeview(frame, columns=columns, show='headings')
tree.heading('Fecha', text='Fecha')
tree.heading('Hora', text='Hora')
tree.heading('Descripción', text='Descripción')
tree.pack(pady=10)

# Frame para las entradas
frame_entradas = tk.Frame(ventana)
frame_entradas.pack(pady=10)

# Campo de selección de fecha (DatePicker)
tk.Label(frame_entradas, text="Fecha:").grid(row=0, column=0)
date_entry = DateEntry(frame_entradas, width=15, background="darkblue", foreground="white", date_pattern='y-mm-dd')
date_entry.grid(row=0, column=1, padx=10)

# Campo de entrada para la hora
tk.Label(frame_entradas, text="Hora:").grid(row=1, column=0)
hora_entry = tk.Entry(frame_entradas, width=20)
hora_entry.grid(row=1, column=1, padx=10)

# Campo de entrada para la descripción
tk.Label(frame_entradas, text="Descripción:").grid(row=2, column=0)
descripcion_entry = tk.Entry(frame_entradas, width=20)
descripcion_entry.grid(row=2, column=1, padx=10)

# Frame para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# Botón para agregar evento
agregar_btn = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
agregar_btn.grid(row=0, column=0, padx=10)

# Botón para eliminar evento
eliminar_btn = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
eliminar_btn.grid(row=0, column=1, padx=10)

# Botón para salir de la aplicación
salir_btn = tk.Button(frame_botones, text="Salir", command=salir)
salir_btn.grid(row=0, column=2, padx=10)

# Iniciar el loop de la ventana
ventana.mainloop()
