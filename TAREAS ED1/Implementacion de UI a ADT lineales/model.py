# model.py

class ConjuntoModel:
    def __init__(self):
        self.conjunto = set()

    def agregar(self, elemento):
        self.conjunto.add(elemento)

    def union(self, otro):
        return self.conjunto.union(otro.conjunto)

    def interseccion(self, otro):
        return self.conjunto.intersection(otro.conjunto)

    def diferencia(self, otro):
        return self.conjunto.difference(otro.conjunto)


class PolinomioModel:
    def __init__(self, coeficientes=None):
        # coeficientes = lista donde índice es el grado del término
        self.coeficientes = coeficientes if coeficientes else []

    def evaluar(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self.coeficientes))

    def sumar(self, otro):
        max_len = max(len(self.coeficientes), len(otro.coeficientes))
        resultado = [0] * max_len
        for i in range(max_len):
            a = self.coeficientes[i] if i < len(self.coeficientes) else 0
            b = otro.coeficientes[i] if i < len(otro.coeficientes) else 0
            resultado[i] = a + b
        return PolinomioModel(resultado)
