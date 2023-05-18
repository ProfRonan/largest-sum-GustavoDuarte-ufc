"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
    """Encontra e retorna os dois números que somados dão o maior valor."""
    numbers.sort()
    a = len(numbers)
    if a < 2:
        print(None)
    else:
        primeiro = numbers[a-1]  # o primeiro número da soma
        segundo = numbers[a-2]  # o segundo número da soma
        print(f"({segundo}, {primeiro})")
    return numbers
lista = []
largest_sum(lista)