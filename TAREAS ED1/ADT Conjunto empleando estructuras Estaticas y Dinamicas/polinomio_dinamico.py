from adt_polinomio import ADTPolinomio

class Nodo:
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp
        self.sig = None

class PolinomioDinamico(ADTPolinomio):
    def __init__(self):
        self.cabeza = None

    def insertar(self, coef, exp):
        nuevo = Nodo(coef, exp)
        if self.cabeza is None or self.cabeza.exp < exp:
            nuevo.sig = self.cabeza
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.sig and actual.sig.exp >= exp:
            actual = actual.sig
        nuevo.sig = actual.sig
        actual.sig = nuevo

    def eliminar(self, exp):
        if not self.cabeza:
            return
        if self.cabeza.exp == exp:
            self.cabeza = self.cabeza.sig
            return
        actual = self.cabeza
        while actual.sig and actual.sig.exp != exp:
            actual = actual.sig
        if actual.sig:
            actual.sig = actual.sig.sig

    def get_coef(self, exp):
        actual = self.cabeza
        while actual:
            if actual.exp == exp:
                return actual.coef
            actual = actual.sig
        return 0

    def set_coef(self, coef, exp):
        actual = self.cabeza
        while actual:
            if actual.exp == exp:
                actual.coef = coef
                return
            actual = actual.sig
        self.insertar(coef, exp)

    def evaluar(self, x):
        resultado = 0
        actual = self.cabeza
        while actual:
            resultado += actual.coef * (x ** actual.exp)
            actual = actual.sig
        return resultado

    def mostrar(self):
        actual = self.cabeza
        pol = []
        while actual:
            pol.append(f"{actual.coef}x^{actual.exp}")
            actual = actual.sig
        return " + ".join(pol) if pol else "0"
