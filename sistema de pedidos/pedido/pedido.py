

from envios.metodo_envio import MetodoEnvio

class Pedido:
    def __init__(self, items: list, peso_total_kg: float):
        self.items = items
        self.peso_total_kg = peso_total_kg
        self.metodo_envio: MetodoEnvio = None

    def asignar_metodo_envio(self, metodo: MetodoEnvio):
        self.metodo_envio = metodo

    def obtener_resumen_envio(self):
        if not self.metodo_envio:
            return "No se ha asignado un método de envío."
        costo = self.metodo_envio.calcular_costo(self.peso_total_kg)
        descripcion = self.metodo_envio.describir_envio()
        return (f"Resumen del Envío:\n"
                f"  Peso del paquete: {self.peso_total_kg} kg\n"
                f"  Método: {descripcion}\n"
                f"  Costo total del envío: ${costo:.2f}")
