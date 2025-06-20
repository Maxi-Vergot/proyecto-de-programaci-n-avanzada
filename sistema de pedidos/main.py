

import sys
import os

# Asegura que el directorio base esté en el path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pedidos.pedido import Pedido
from envios.envio_estandar import EnvioEstandar
from envios.envio_express import EnvioExpress
from envios.envio_prioritario import EnvioPrioritario
from envios.con_seguro_envio import ConSeguroEnvio
from envios.con_embalaje_regalo import ConEmbalajeRegalo
from envios.decorador_descuento import aplicar_cupon



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
    while True:
        respuesta = input("¿Desea añadir Seguro al envío? (s/n): ").strip().lower()
        if respuesta == "s":
            envio = ConSeguroEnvio(envio)
            break
        elif respuesta == "n":
            break
        else:
            print("Entrada inválida. Por favor, ingrese 's' o 'n'.")

    while True:
        respuesta = input("¿Desea añadir Embalaje de Regalo? (s/n): ").strip().lower()
        if respuesta == "s":
            envio = ConEmbalajeRegalo(envio)
            break
        elif respuesta == "n":
            break
        else:
            print("Entrada inválida. Por favor, ingrese 's' o 'n'.")

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
    input("\nPresione Enter para cerrar...")
