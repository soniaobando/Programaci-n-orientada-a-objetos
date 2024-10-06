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
        self.scrollbar.config(command=self.task_listbox.y
