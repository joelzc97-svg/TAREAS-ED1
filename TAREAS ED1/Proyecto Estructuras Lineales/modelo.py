class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None


class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.frente = self.final = nuevo
        else:
            self.final.sig = nuevo
            self.final = nuevo

    def desencolar(self):
        if self.esta_vacia():
            return None
        dato = self.frente.dato
        self.frente = self.frente.sig
        if self.frente is None:
            self.final = None
        return dato

    def obtener_todos(self):
        elementos = []
        aux = self.frente
        while aux:
            elementos.append(aux.dato)
            aux = aux.sig
        return elementos
