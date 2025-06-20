

from abc import ABC
from envios.metodo_envio import MetodoEnvio

class EnvioDecorador(MetodoEnvio, ABC):
    def __init__(self, envio_base: MetodoEnvio):
        super().__init__(envio_base.nombre_metodo)
        self._envio_base = envio_base
