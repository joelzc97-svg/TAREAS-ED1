from conjunto_estatico import ConjuntoEstatico
from conjunto_dinamico import ConjuntoDinamico

def probar_conjunto(conjunto, nombre):
    print(f"\n=== Probando {nombre} ===")

    conjunto.agregar(10)
    conjunto.agregar(20)
    conjunto.agregar(30)
    conjunto.agregar(20)  # duplicado

    print("Elementos iniciales:", conjunto.get_elementos())
    print("Tamaño:", conjunto.get_tamaño())

    conjunto.eliminar(20)
    print("Después de eliminar 20:", conjunto.get_elementos())
    print("Tamaño:", conjunto.get_tamaño())

    conjunto.set_elementos([5, 15, 25])
    print("Después de set_elementos:", conjunto.get_elementos())
    print("Tamaño:", conjunto.get_tamaño())


if __name__ == "__main__":
    ce = ConjuntoEstatico(5)
    cd = ConjuntoDinamico()

    probar_conjunto(ce, "Conjunto Estático")
    probar_conjunto(cd, "Conjunto Dinámico")
