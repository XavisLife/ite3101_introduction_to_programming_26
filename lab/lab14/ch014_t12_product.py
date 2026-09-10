def product(numbers: list[int]) -> int:
    total = 1
    for number in numbers:
        total *= number
    return total
