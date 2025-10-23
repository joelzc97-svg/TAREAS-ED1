import tkinter as tk
from tkinter import messagebox

class Vista:
    def __init__(self, root, controlador):
        self.controlador = controlador

        root.title("Simulador de Fila (Caja / Plataforma)")
        root.geometry("400x350")
        root.config(bg="#f4f4f4")

        tk.Label(root, text="Fila de Espera", font=("Arial", 18, "bold"), bg="#f4f4f4").pack(pady=10)

        # Botones principales
        tk.Button(root, text="Caja", command=lambda: self.controlador.agregar_cliente("caja"),
                  bg="#2196F3", fg="white", font=("Arial", 12, "bold"), width=12).pack(pady=5)

        tk.Button(root, text="Plataforma", command=lambda: self.controlador.agregar_cliente("plataforma"),
                  bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=12).pack(pady=5)

        # Botón de atender
        tk.Button(root, text="Atender Siguiente", command=self.controlador.atender_cliente,
                  bg="#FFC107", fg="black", font=("Arial", 12, "bold"), width=15).pack(pady=10)

        # Lista visual de la cola
        self.lista = tk.Listbox(root, width=30, height=10, font=("Arial", 12))
        self.lista.pack(pady=10)

    def actualizar_lista(self, clientes):
        self.lista.delete(0, tk.END)
        for c in clientes:
            self.lista.insert(tk.END, c)

    def mostrar_mensaje(self, texto):
        messagebox.showinfo("Información", texto)
