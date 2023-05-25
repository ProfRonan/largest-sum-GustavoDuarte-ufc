def largest_sum(numbers: list[int]) -> tuple[int, int]:
    numbers.sort()
    a = len(numbers)
    if a < 2:
        return None
    else:
        primeiro = numbers[a-1]  # o primeiro número da soma
        segundo = numbers[a-2]  # o segundo número da soma
        resultado_esperado = (segundo, primeiro)
        return resultado_esperado