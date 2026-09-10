def median(numbers: list[int]) -> float:
    sorted_list = numbers.sort()
    middle = len(sorted_list) // 2
    if len(sorted_list) % 2 == 0:
        return (sorted_list[middle - 1] + sorted_list[middle])