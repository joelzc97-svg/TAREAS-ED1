from abc import ABC, abstractmethod

class ADTPolinomio(ABC):
    @abstractmethod
    def insertar(self, coef, exp):
        pass

    @abstractmethod
    def eliminar(self, exp):
        pass

    @abstractmethod
    def get_coef(self, exp):
        pass

    @abstractmethod
    def set_coef(self, coef, exp):
        pass

    @abstractmethod
    def evaluar(self, x):
        pass

    @abstractmethod
    def mostrar(self):
        pass
