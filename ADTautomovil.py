class Automovil:
    def __init__(self, marca, modelo, anio):
        self.__marca = marca   # Atributos privados
        self.__modelo = modelo
        self.__anio = anio

    # --- Getters ---
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_anio(self):
        return self.__anio

    # --- Setters ---
    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_anio(self, anio):
        self.__anio = anio

    def __str__(self):
        return f"{self.__marca} {self.__modelo} ({self.__anio})"


# ---- Lista Estática de Automóviles ----
class ListaEstaticaAutomoviles:
    def __init__(self, max_size=3):
        self.max_size = max_size
        self.lista = [None] * max_size  # Espacio reservado
        self.cantidad = 0

    def insertar(self, auto):
        if self.cantidad < self.max_size:
            self.lista[self.cantidad] = auto
            self.cantidad += 1
        else:
            print("⚠️ Lista llena (estática)")

    def mostrar(self):
        for i in range(self.cantidad):
            print(self.lista[i])


# ---- Ejemplo ----
auto1 = Automovil("Toyota", "Corolla", 2020)
auto2 = Automovil("Ford", "Focus", 2018)
auto3 = Automovil("Chevrolet", "Onix", 2021)

lista_estatica = ListaEstaticaAutomoviles(max_size=3)
lista_estatica.insertar(auto1)
lista_estatica.insertar(auto2)
lista_estatica.insertar(auto3)
lista_estatica.mostrar()
