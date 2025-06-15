

from .metodo_envio import MetodoEnvio

class EnvioPrioritario(MetodoEnvio):
    def __init__(self):
        super().__init__("Envío Prioritario")
        self.tarifa_base = 25.0
        self.costo_por_kg = 8.0

    def calcular_costo(self, peso_kg: float) -> float:
        return self.tarifa_base + (self.costo_por_kg * peso_kg)

    def describir_envio(self) -> str:
        return "Envío Prioritario: Entrega en 24 horas garantizada."