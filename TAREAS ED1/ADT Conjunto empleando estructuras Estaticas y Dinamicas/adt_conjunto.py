from abc import ABC, abstractmethod

class ADTConjunto(ABC):
    """Interfaz abstracta de un Conjunto"""

    @abstractmethod
    def agregar(self, valor): pass

    @abstractmethod
    def eliminar(self, valor): pass

    @abstractmethod
    def contiene(self, valor): pass

    @abstractmethod
    def get_elementos(self): pass

    @abstractmethod
    def set_elementos(self, elementos): pass

    @abstractmethod
    def get_tamaño(self): pass
