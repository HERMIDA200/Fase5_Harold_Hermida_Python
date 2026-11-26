"""
Solución Problema 3: Inventario de artículos
Curso: Fundamentos de Programación (213022) - Fase 5 (Evaluación Final POA)
"""


def calcular_cantidad_a_pedir(stock_actual: int, stock_minimo: int) -> int:
    """
    Calcula la cantidad exacta a pedir para reabastecer un artículo.

    Regla:
    - Si stock_actual < stock_minimo: retorna (stock_minimo - stock_actual).
    - Si stock_actual >= stock_minimo: retorna 0.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def mostrar_reporte_inventario(inventario: list[list]) -> None:
    """
    Recorre la matriz de inventario y muestra el nombre de cada artículo
    junto con la cantidad exacta que debe solicitarse.
    """
    print("\n=== REPORTE DE REABASTECIMIENTO DE INVENTARIO ===")
    for articulo in inventario:
        # Formato esperado: [Código, Nombre, Stock actual, Stock mínimo requerido]
        _codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        print(f"Artículo: {nombre} | Cantidad a solicitar: {cantidad_pedir}")


def main() -> None:
    """Ejecuta el proceso de evaluación del inventario."""
    # Matriz con 5 artículos: [Código del artículo, Nombre, Stock actual, Stock mínimo requerido]
    inventario = [
        ["ART-01", "Teclado mecánico", 4, 10],     # Faltan 6 unidades
        ["ART-02", "Mouse inalámbrico", 15, 12],   # Stock suficiente -> 0
        ["ART-03", "Cable HDMI", 8, 8],            # Igual al mínimo -> 0
        ["ART-04", "Monitor 24 pulgadas", 2, 6],   # Faltan 4 unidades
        ["ART-05", "Memoria USB 64GB", 9, 15],     # Faltan 6 unidades
    ]

    mostrar_reporte_inventario(inventario)


if __name__ == "__main__":
    main()