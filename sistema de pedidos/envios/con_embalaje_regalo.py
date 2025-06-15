

from .envio_decorador import EnvioDecorador

class ConEmbalajeRegalo(EnvioDecorador):
    def __init__(self, envio_base, costo_embalaje=4.5):
        super().__init__(envio_base)
        self.costo_embalaje = costo_embalaje

    def calcular_costo(self, peso_kg: float) -> float:
        return self._envio_base.calcular_costo(peso_kg) + self.costo_embalaje

    def describir_envio(self) -> str:
        return f"{self._envio_base.describir_envio()} + Embalaje de Regalo"