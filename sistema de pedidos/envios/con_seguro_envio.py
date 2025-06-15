

from .envio_decorador import EnvioDecorador

class ConSeguroEnvio(EnvioDecorador):
    def __init__(self, envio_base, costo_seguro=3.0):
        super().__init__(envio_base)
        self.costo_seguro = costo_seguro

    def calcular_costo(self, peso_kg: float) -> float:
        return self._envio_base.calcular_costo(peso_kg) + self.costo_seguro

    def describir_envio(self) -> str:
        return f"{self._envio_base.describir_envio()} + Seguro de Envío"