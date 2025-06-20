

from envios.metodo_envio import MetodoEnvio

class EnvioExpress(MetodoEnvio):
    def __init__(self):
        super().__init__("Envío Express")
        self.tarifa_base = 15.0
        self.costo_por_kg = 5.0

    def calcular_costo(self, peso_kg: float) -> float:
        return self.tarifa_base + (self.costo_por_kg * peso_kg)

    def describir_envio(self) -> str:
        return "Envío Express: Entrega en 1-2 días hábiles."
