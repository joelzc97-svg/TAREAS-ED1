from adt_polinomio import ADTPolinomio

class PolinomioEstatico(ADTPolinomio):
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.terminos = []  # lista de tuplas (coef, exp)

    def insertar(self, coef, exp):
        if len(self.terminos) >= self.capacidad:
            print("Capacidad máxima alcanzada")
            return
        self.terminos.append((coef, exp))

    def eliminar(self, exp):
        self.terminos = [(c, e) for (c, e) in self.terminos if e != exp]

    def get_coef(self, exp):
        for (c, e) in self.terminos:
            if e == exp:
                return c
        return 0

    def set_coef(self, coef, exp):
        for i, (c, e) in enumerate(self.terminos):
            if e == exp:
                self.terminos[i] = (coef, exp)
                return
        self.insertar(coef, exp)

    def evaluar(self, x):
        return sum(c * (x ** e) for (c, e) in self.terminos)

    def mostrar(self):
        pol = " + ".join(f"{c}x^{e}" for (c, e) in sorted(self.terminos, key=lambda t: -t[1]))
        return pol if pol else "0"
