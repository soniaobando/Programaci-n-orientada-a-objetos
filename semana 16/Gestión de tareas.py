import tkinter as tk
from tkinter import messagebox, simpledialog


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Lista de tareas
        self.tasks = []

        # Frame para las tareas
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT)

        # Barra de desplazamiento
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Campo de entrada para añadir nuevas tareas
        self.task_entry = tk.Entry(self.root, width=52)
        self.task_entry.pack(pady=10)

        # Botones
        self.add_task_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Configuración de atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())  # Añadir tarea con Enter
        self.root.bind('<c>', lambda event: self.complete_task())  # Marcar tarea como completada con 'C'
        self.root.bind('<Delete>', lambda event: self.delete_task())  # Eliminar tarea con 'Delete'
        self.root.bind('<Escape>', lambda event: self.root.quit())  # Cerrar aplicación con Esc

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            completed_task = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = f"{completed_task} - Completada"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)  # Limpiar la lista actual
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Agregar las tareas a la lista


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()




