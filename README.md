# Sistema de Pedidos y Envíos

Este proyecto simula un sistema de pedidos donde el usuario puede cargar una lista de productos, elegir entre distintos métodos de envío y agregar algunas opciones extra, como seguro o embalaje de regalo. También se puede aplicar un cupón de descuento si el usuario lo desea. Todo funciona desde una interfaz por consola, sin necesidad de conexión a internet ni instalación de librerías externas.

---

Durante el desarrollo trabajamos con programación orientada a objetos, organizando las clases en distintos módulos según su función. Usamos herencia, clases abstractas y decoradores para estructurar el código y permitir agregar funcionalidades de forma flexible, sin modificar lo ya hecho. También aplicamos una lógica de diseño que permite que el sistema sea escalable y fácil de mantener.

---

## ¿Cómo está organizado?

El proyecto está dividido en tres partes principales:

- **envios/**: contiene los distintos métodos de envío (estándar, express y prioritario) y las opciones adicionales como seguro y embalaje. También está el decorador funcional que aplica el descuento del cupón.

- **pedidos/**: contiene la clase `Pedido`, que representa el conjunto de productos y su método de envío.

- **main.py**: es el archivo principal desde donde se corre el sistema y el usuario interactúa.

Una vez generado, el ejecutable se puede compartir con otras personas sin necesidad de que tengan Python instalado.

Requisitos

- No es necesario tener Python instalado si se utiliza el ejecutable
- En caso de ejecutar desde código fuente: Python 3.10 o superior

---

Ejecución del Sistema

### Opción 1: Ejecutable (.exe)

1. Hacer doble clic sobre el archivo `sistema-pedidos.exe`.
2. El sistema se ejecutará en una ventana de consola y podrá ser utilizado de manera interactiva.

No se requiere instalación ni dependencias. El ejecutable funciona de forma autónoma en cualquier computadora con Windows.

---

### Opción 2: Desde código fuente (solo si es necesario)

```bash
python main.py
