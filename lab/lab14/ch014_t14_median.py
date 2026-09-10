def median(numbers: list[int]) -> float:
    numbers.sort()
    middle = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[middle - 1] + numbers[middle]) / 2
    else:
        return numbers[middle]
