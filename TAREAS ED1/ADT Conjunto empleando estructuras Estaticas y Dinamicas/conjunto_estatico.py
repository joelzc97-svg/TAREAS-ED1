from adt_conjunto import ADTConjunto

class ConjuntoEstatico(ADTConjunto):
    def __init__(self, capacidad):
        self.CAPACIDAD_MAX = capacidad
        self.elementos = []

    def agregar(self, valor):
        if len(self.elementos) < self.CAPACIDAD_MAX and valor not in self.elementos:
            self.elementos.append(valor)
            return True
        return False

    def eliminar(self, valor):
        if valor in self.elementos:
            self.elementos.remove(valor)
            return True
        return False

    def contiene(self, valor):
        return valor in self.elementos

    def get_elementos(self):
        return self.elementos.copy()

    def set_elementos(self, elementos):
        # Mantener sin duplicados y respetar capacidad
        self.elementos = list(dict.fromkeys(elementos))[:self.CAPACIDAD_MAX]

    def get_tamaño(self):
        return len(self.elementos)
