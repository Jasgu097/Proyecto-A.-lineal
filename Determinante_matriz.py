"""
def determinante_matriz(matriz):
    """
"""
    Calcula la determinante de una matriz cuadrada utilizando el método de eliminación gaussiana.

    Args:
        matriz (list of lists): La matriz cuadrada de la cual se calculará la determinante.

    Returns:
        float: El valor de la determinante de la matriz.
    n = len(matriz)

    # Si la matriz es de 1x1, la determinante es simplemente el único elemento.
    if n == 1:
        return matriz[0][0]

    # Inicializamos la determinante como 0.
    det = 0

    # Para cada columna 'j' en la primera fila de la matriz, calculamos la cofactor y sumamos
    # o restamos dependiendo del índice de la columna.
    for j in range(n):
        det += matriz[0][j] * cofactor(matriz, 0, j)

    return det


def cofactor(matriz, fila, columna):
"""
"""
    Calcula el cofactor de un elemento en una matriz.

    Args:
        matriz (list of lists): La matriz de la cual se calculará el cofactor.
        fila (int): El índice de la fila del elemento.
        columna (int): El índice de la columna del elemento.

    Returns:
        float: El valor del cofactor del elemento.
    """
"""
    submatriz = [fila[:columna] + fila[columna + 1:] for fila in (matriz[:fila] + matriz[fila + 1:])]
    return (-1) ** (fila + columna) * determinante_matriz(submatriz)


# Ejemplo de uso:
matriz_ejemplo = [
    [4, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("La determinante de la matriz es:", determinante_matriz(matriz_ejemplo))
"""
print("Aun no implementado")