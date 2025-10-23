from modelo import Cola
class Controlador:
    def __init__(self, vista):
        self.vista = vista
        self.cola = Cola()

        # Contadores
        self.contador_caja = 0
        self.contador_plataforma = 0

        # Alternadores
        self.caja_actual = 1
        self.plataforma_actual = 1

    def agregar_cliente(self, tipo):
        if tipo == "caja":
            self.contador_caja += 1
            codigo = f"C{self.contador_caja} = Caja_{self.caja_actual}"
            # Alternar entre Caja 1 y Caja 2
            self.caja_actual = 2 if self.caja_actual == 1 else 1

        elif tipo == "plataforma":
            self.contador_plataforma += 1
            codigo = f"P{self.contador_plataforma} = Plataforma_{self.plataforma_actual}"
            # Alternar entre Plataforma 1 y Plataforma 2
            self.plataforma_actual = 2 if self.plataforma_actual == 1 else 1

        else:
            return

        self.cola.encolar(codigo)
        self.vista.actualizar_lista(self.cola.obtener_todos())

    def atender_cliente(self):
        cliente = self.cola.desencolar()
        if cliente:
            self.vista.mostrar_mensaje(f"Atendiendo a {cliente}")
        else:
            self.vista.mostrar_mensaje("No hay nadie en la fila.")
        self.vista.actualizar_lista(self.cola.obtener_todos())
