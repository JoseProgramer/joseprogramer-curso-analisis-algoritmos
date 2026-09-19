def calcular_promedio(lista_numeros: list[float]) -> float:
    """
    Calcula el promedio de una lista de números.

    Args:
        lista_numeros: Lista de valores numéricos.

    Returns:
        Promedio de los valores recibidos.
    """

    suma = 0

    for numero in lista_numeros:
        suma = suma + numero

    return suma / len(lista_numeros)


def main() -> None:
    numeros = [1, 2, 3, 4, 5]
    print(calcular_promedio(numeros))


if __name__ == "__main__":
    main()