from polinomio_estatico import PolinomioEstatico
from polinomio_dinamico import PolinomioDinamico

def main():
    print("==== PRUEBAS DE POLINOMIOS ====")

    # Polinomio Estático
    pe = PolinomioEstatico()
    pe.insertar(3, 2)  # 3x^2
    pe.insertar(2, 1)  # 2x^1
    pe.insertar(5, 0)  # 5
    print("Polinomio Estático:", pe.mostrar())
    print("Evaluar en x=2:", pe.evaluar(2))

    # Polinomio Dinámico
    pd = PolinomioDinamico()
    pd.insertar(4, 3)  # 4x^3
    pd.insertar(1, 1)  # 1x^1
    pd.insertar(7, 0)  # 7
    print("Polinomio Dinámico:", pd.mostrar())
    print("Evaluar en x=2:", pd.evaluar(2))

if __name__ == "__main__":
    main()
