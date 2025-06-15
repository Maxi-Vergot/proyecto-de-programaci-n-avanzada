

from abc import ABC, abstractmethod

class MetodoEnvio(ABC):
    def __init__(self, nombre_metodo):
        self.nombre_metodo = nombre_metodo

    @abstractmethod
    def calcular_costo(self, peso_kg: float) -> float:
        pass

    @abstractmethod
    def describir_envio(self) -> str:
        pass