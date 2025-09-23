# controller.py

from model import ConjuntoModel, PolinomioModel

class MainController:
    def __init__(self, view):
        self.view = view
        # No guardamos modelos globales todavía, se crean al operar

    # ---------------- OPERACIONES CONJUNTOS ----------------
    def operar_conjuntos(self, operacion):
        try:
            # Leer entradas y convertir a sets de enteros
            a = set(map(int, self.view.ids.conjunto_a.text.split(",")))
            b = set(map(int, self.view.ids.conjunto_b.text.split(",")))

            conjunto_a = ConjuntoModel()
            conjunto_a.conjunto = a
            conjunto_b = ConjuntoModel()
            conjunto_b.conjunto = b

            if operacion == "union":
                res = conjunto_a.union(conjunto_b)
            elif operacion == "interseccion":
                res = conjunto_a.interseccion(conjunto_b)
            elif operacion == "diferencia":
                res = conjunto_a.diferencia(conjunto_b)
            else:
                res = set()

            # Mostrar resultado en la vista
            self.view.ids.resultado_conjuntos.text = f"Resultado: {res}"
        except Exception as e:
            self.view.ids.resultado_conjuntos.text = f"Error: {e}"

    # ---------------- OPERACIONES POLINOMIOS ----------------
    def operar_polinomios(self, operacion):
        try:
            # Leer coeficientes de la vista y convertir a listas de floats
            coefs_a = list(map(float, self.view.ids.polinomio_a.text.split(",")))
            coefs_b = list(map(float, self.view.ids.polinomio_b.text.split(",")))

            poli_a = PolinomioModel(coefs_a)
            poli_b = PolinomioModel(coefs_b)

            if operacion == "sumar":
                resultado = poli_a.sumar(poli_b)
                self.view.ids.resultado_polinomios.text = f"Resultado: {resultado.coeficientes}"
            elif operacion == "evaluar":
                x = 2  # valor fijo por ahora, se puede modificar para input
                valor = poli_a.evaluar(x)
                self.view.ids.resultado_polinomios.text = f"P({x}) = {valor}"
            else:
                self.view.ids.resultado_polinomios.text = "Operación desconocida"
        except Exception as e:
            self.view.ids.resultado_polinomios.text = f"Error: {e}"
