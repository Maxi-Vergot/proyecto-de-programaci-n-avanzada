

def aplicar_cupon(descuento: float):
    """
    Decorador que aplica un porcentaje de descuento al costo del envío.
    descuento: número entre 0 y 1 (por ejemplo, 0.10 para 10%)
    """
    def decorador(func):
        def wrapper(peso_kg):
            costo_original = func(peso_kg)
            costo_final = costo_original * (1 - descuento)
            return round(costo_final, 2)
        return wrapper
    return decorador

