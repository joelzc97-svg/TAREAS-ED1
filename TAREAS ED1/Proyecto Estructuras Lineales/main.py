import tkinter as tk
from vista import Vista 
from controlador import Controlador 

if __name__ == "__main__":
    root = tk.Tk()
    controlador = Controlador(None)
    vista = Vista(root, controlador)
    controlador.vista = vista
    root.mainloop()
