from pedido import Pedido
from envios import (
    EnvioEstandar,
    EnvioExpress,
    EnvioPrioritario,
    ConSeguroEnvio,
    ConEmbalajeRegalo,
    aplicar_cupon
)
from typing import Optional, List
# se utiliza el modulo typing para anotar listas con elementos de un tipo específico.
# Se usa cuando una variable, parámetro o retorno puede ser opcional (es decir, admite None)

# === CONSTANTES DE MENSAJES ===
MENU_ENVIO = """
Seleccione un método de envío:
1. Envío Estándar
2. Envío Express
3. Envío Prioritario
"""

PREGUNTA_SEGURO = "¿Desea añadir Seguro al envío? (s/n)"
PREGUNTA_REGALO = "¿Desea añadir Embalaje de Regalo? (s/n)"
PREGUNTA_CUPON = "¿Tiene un cupón de descuento? (s/n)"
PESO_INPUT = "Ingrese el peso total del paquete en kg ('s' para salir): "
ITEMS_INPUT = "Ingrese los productos separados por coma ('s' para salir): "

# === FUNCIONES AUXILIARES ===

def obtener_items() -> Optional[List[str]]:
    while True:
        try:
            items_input = input(ITEMS_INPUT).strip().lower()
            if items_input == 's':
                print("Operación cancelada. Saliendo...")
                return None
            items = [item.strip() for item in items_input.split(",")]
            items = [item for item in items if item]
            if not items:
                print("Debe ingresar al menos un producto.")
                continue
            return items
        except Exception as e:
            print(f"Error al procesar productos: {e}. Intente nuevamente.")

def obtener_peso() -> Optional[float]:
    while True:
        try:
            peso_input = input(PESO_INPUT).strip().lower()
            if peso_input == 's':
                print("Operación cancelada. Saliendo...")
                return None
            peso = float(peso_input)
            if peso <= 0:
                print("El peso debe ser mayor a 0. Intente nuevamente.")
            else:
                return peso
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

def seleccionar_metodo_envio() -> Optional[object]:
    print(MENU_ENVIO)
    opcion = input("Ingrese su opción (1-3) o 's' para salir: ").strip().lower()
    if opcion == "s":
        print("Saliendo del sistema...")
        return None

    if opcion == "1":
        return EnvioEstandar()
    elif opcion == "2":
        return EnvioExpress()
    elif opcion == "3":
        return EnvioPrioritario()
    else:
        print("Opción inválida. Se usará Envío Estándar por defecto.")
        return EnvioEstandar()

def aplicar_decoradores(envio: object) -> object:
    print(PREGUNTA_SEGURO)
    if input("> ").strip().lower() == "s":
        envio = ConSeguroEnvio(envio)

    print(PREGUNTA_REGALO)
    if input("> ").strip().lower() == "s":
        envio = ConEmbalajeRegalo(envio)

    return envio

def aplicar_descuento_si_corresponde(envio: object) -> object:
    print(PREGUNTA_CUPON)
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

# === FUNCIÓN PRINCIPAL ===
def main():
    print("=== Sistema de Envío de Pedidos ===")
    
    # Obtener items
    items = obtener_items()
    if items is None:
        return

    # Obtener peso
    peso = obtener_peso()
    if peso is None:
        return

    pedido = Pedido(items=items, peso_total_kg=peso)

    # Seleccionar método de envío
    envio = seleccionar_metodo_envio()
    if envio is None:
        return

    # Aplicar decoradores
    envio = aplicar_decoradores(envio)
    envio = aplicar_descuento_si_corresponde(envio)

    pedido.asignar_metodo_envio(envio)

    print("\n" + pedido.obtener_resumen_envio())

# === EJECUCIÓN ===
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")