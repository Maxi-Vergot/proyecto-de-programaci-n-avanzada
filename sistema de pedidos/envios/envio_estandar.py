

from envios.metodo_envio import MetodoEnvio

class EnvioEstandar(MetodoEnvio):
    def __init__(self):
        super().__init__("Envío Estándar")
        self.tarifa_base = 5.0
        self.costo_por_kg = 2.0

    def calcular_costo(self, peso_kg: float) -> float:
        return self.tarifa_base + (self.costo_por_kg * peso_kg)

    def describir_envio(self) -> str:
        return "Envío Estándar: Entrega en 5-7 días hábiles."
