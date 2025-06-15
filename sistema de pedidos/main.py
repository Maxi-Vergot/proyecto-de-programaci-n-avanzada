

from pedido import Pedido
from envios import (
    EnvioEstandar,
    EnvioExpress,
    EnvioPrioritario,
    ConSeguroEnvio,
    ConEmbalajeRegalo
)


def seleccionar_metodo_envio():
    print("Seleccione un método de envío:")
    print("1. Envío Estándar")
    print("2. Envío Express")
    print("3. Envío Prioritario")
    opcion = input("Opción (1-3): ").strip()

    if opcion == "1":
        return EnvioEstandar()
    elif opcion == "2":
        return EnvioExpress()
    elif opcion == "3":
        return EnvioPrioritario()
    else:
        print("Opción inválida. Se usará Envío Estándar por defecto.")
        return EnvioEstandar()

def aplicar_decoradores(envio):
    print("¿Desea añadir Seguro al envío? (s/n)")
    if input("> ").strip().lower() == "s":
        envio = ConSeguroEnvio(envio)

    print("¿Desea añadir Embalaje de Regalo? (s/n)")
    if input("> ").strip().lower() == "s":
        envio = ConEmbalajeRegalo(envio)

    return envio

def main():
    print("=== Sistema de Envío de Pedidos ===")
    items = input("Ingrese los productos separados por coma: ").split(",")
    try:
        peso = float(input("Ingrese el peso total del paquete en kg: "))
    except ValueError:
        print("Peso inválido. Se usará 1.0 kg por defecto.")
        peso = 1.0

    pedido = Pedido(items=items, peso_total_kg=peso)

    envio = seleccionar_metodo_envio()
    envio = aplicar_decoradores(envio)

    pedido.asignar_metodo_envio(envio)
    print("\n" + pedido.obtener_resumen_envio())

if __name__ == "__main__":
    main()