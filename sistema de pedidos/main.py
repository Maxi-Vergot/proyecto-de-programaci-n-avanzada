

from pedido import Pedido
from envios import (
    EnvioEstandar,
    EnvioExpress,
    EnvioPrioritario,
    ConSeguroEnvio,
    ConEmbalajeRegalo,
    aplicar_cupon
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

def aplicar_descuento_si_corresponde(envio):
    print("¿Tiene un cupón de descuento? (s/n)")
    if input("> ").strip().lower() == "s":
        while True:
            try:
                porcentaje = int(input("Ingrese porcentaje de descuento (ej. 10 para 10%): "))
                if 0 < porcentaje < 100:
                    envio.calcular_costo = aplicar_cupon(porcentaje / 100)(envio.calcular_costo)
                    break
                else:
                    print("Debe ingresar un número entre 1 y 99.")
            except ValueError:
                print("Entrada no válida. Intente nuevamente.")
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
    envio = aplicar_descuento_si_corresponde(envio)

    pedido.asignar_metodo_envio(envio)

    print("\n" + pedido.obtener_resumen_envio())

if __name__ == "__main__":
    main()