from adt_conjunto import ADTConjunto

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ConjuntoDinamico(ADTConjunto):
    def __init__(self):
        self.cabeza = None
        self.tamaño = 0

    def agregar(self, valor):
        if self.contiene(valor):
            return False
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True

    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.valor == valor:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.tamaño -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def contiene(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def get_elementos(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos

    def set_elementos(self, elementos):
        self.cabeza = None
        self.tamaño = 0
        for v in elementos:
            self.agregar(v)

    def get_tamaño(self):
        return self.tamaño
