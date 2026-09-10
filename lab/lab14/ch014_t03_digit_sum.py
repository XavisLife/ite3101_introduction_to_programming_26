# Conversion version
'''
def digit_sum(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total
'''

# Challenging version


def digit_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + digit_sum(n // 10)
