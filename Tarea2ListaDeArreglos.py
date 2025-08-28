class Lista:
    def __init__(self, max_size=100):
        self.elem = []  # Lista de elementos
        self.max = max_size

    # Ejercicio 3: Insertar al final
    def insertar_ult(self, x):
        if len(self.elem) < self.max:
            self.elem.append(x)

    # Ejercicio 1: Insertar en lugar ascendente
    def insertar_lugar_asc(self, x):
        i = 0
        while i < len(self.elem) and self.elem[i] < x:
            i += 1
        self.elem.insert(i, x)

    # Ejercicio 2: Insertar en lugar descendente
    def insertar_lugar_desc(self, x):
        i = 0
        while i < len(self.elem) and self.elem[i] > x:
            i += 1
        self.elem.insert(i, x)

    # Ejercicio 3: Elementos comunes con otras listas
    def comunes(self, l2, l3):
        self.elem = [x for x in self.elem if x in l2.elem and x in l3.elem]

    # Ejercicio 4: Intercalar listas
    def intercalar(self, l2, l3):
        inter = []
        for i in range(max(len(l2.elem), len(l3.elem))):
            if i < len(l2.elem):
                inter.append(l2.elem[i])
            if i < len(l3.elem):
                inter.append(l3.elem[i])
        self.elem = inter

    # Ejercicio 5: Ordenado
    def ordenado(self):
        return self.elem == sorted(self.elem) or self.elem == sorted(self.elem, reverse=True)

    # Ejercicio 6: Todos iguales
    def iguales(self):
        return all(x == self.elem[0] for x in self.elem) if self.elem else True

    # Ejercicio 7: Todos diferentes
    def diferentes(self):
        return len(self.elem) == len(set(self.elem))

    # Ejercicio 8: Menor
    def menor(self):
        return min(self.elem) if self.elem else None

    # Ejercicio 9: Par e impar
    def par_impar(self):
        tiene_par = any(x % 2 == 0 for x in self.elem)
        tiene_impar = any(x % 2 != 0 for x in self.elem)
        return tiene_par and tiene_impar

    # Ejercicio 10: Misma frecuencia
    def misma_frec(self):
        if not self.elem:
            return True
        frecs = [self.elem.count(x) for x in set(self.elem)]
        return all(f == frecs[0] for f in frecs)

    # Ejercicio 11: Palindrome
    def palindrome(self):
        return self.elem == self.elem[::-1]

    # Ejercicio 12: Mismos elementos
    def mismos_elem(self, l2):
        return set(self.elem) == set(l2.elem)

    def __str__(self):
        return str(self.elem)

def main():
    # ===== Listas con datos ya cargados =====
    l1 = Lista(20)
    for x in [5, 2, 8, 1, 3]:
        l1.insertar_ult(x)

    l2 = Lista(20)
    for x in [3, 1, 7, 9]:
        l2.insertar_ult(x)

    l3 = Lista(20)
    for x in [1, 2, 3, 4, 5]:
        l3.insertar_ult(x)

    print("Lista L1:", l1)
    print("Lista L2:", l2)
    print("Lista L3:", l3)

    print("\n--- PROBANDO MÉTODOS ---")

    # Ejercicio 1
    l1_asc = Lista(20)
    l1_asc.elem = l1.elem.copy()
    l1_asc.insertar_lugar_asc(0)
    print("\nEjercicio 1 - Insertar 0 en L1 (ascendente):", l1_asc)

    # Ejercicio 2
    l1_desc = Lista(20)
    l1_desc.elem = l1.elem.copy()
    l1_desc.insertar_lugar_desc(99)
    print("Ejercicio 2 - Insertar 99 en L1 (descendente):", l1_desc)

    # Ejercicio 3
    l1_comunes = Lista(20)
    l1_comunes.elem = l1.elem.copy()
    l1_comunes.comunes(l2, l3)
    print("\nEjercicio 3 - Comunes entre L1, L2 y L3:", l1_comunes)

    # Ejercicio 4
    l1_intercalada = Lista(20)
    l1_intercalada.elem = l1.elem.copy()
    l1_intercalada.intercalar(l2, l3)
    print("Ejercicio 4 - Intercalar L2 y L3 en L1:", l1_intercalada)

    # Ejercicio 5
    print("Ejercicio 5 - ¿L1 está ordenada?:", l1.ordenado())

    # Ejercicio 6
    iguales_test = Lista(5)
    for x in [7, 7, 7]:
        iguales_test.insertar_ult(x)
    print("Ejercicio 6 - ¿Todos iguales en [7, 7, 7]?:", iguales_test.iguales())

    # Ejercicio 7
    diferentes_test = Lista(5)
    for x in [1, 2, 3]:
        diferentes_test.insertar_ult(x)
    print("Ejercicio 7 - ¿Todos diferentes en [1, 2, 3]?:", diferentes_test.diferentes())

    # Ejercicio 8
    print("Ejercicio 8 - Menor de L3:", l3.menor())

    # Ejercicio 9
    print("Ejercicio 9 - ¿L3 tiene pares e impares?:", l3.par_impar())

    # Ejercicio 10
    frec_test = Lista(6)
    for x in [2, 2, 3, 3]:
        frec_test.insertar_ult(x)
    print("Ejercicio 10 - ¿[2,2,3,3] misma frecuencia?:", frec_test.misma_frec())

    # Ejercicio 11
    pal_test = Lista(5)
    for x in [1, 2, 3, 2, 1]:
        pal_test.insertar_ult(x)
    print("Ejercicio 11 - ¿[1,2,3,2,1] es palíndrome?:", pal_test.palindrome())

    # Ejercicio 12
    l4 = Lista(5)
    for x in [3, 1, 7, 9]:
        l4.insertar_ult(x)
    print("Ejercicio 12 - ¿L2 y L4 tienen los mismos elementos?:", l2.mismos_elem(l4))

# Ejecutar main
if __name__ == "__main__":
    main()
