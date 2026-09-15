def flip_bit(number, n):
    mask = 1 << n
    result = number ^ mask
    return bin(result)
