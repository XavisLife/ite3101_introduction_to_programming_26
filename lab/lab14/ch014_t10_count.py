def count(sequence, item):
    count = 0
    for value in sequence:
        if value == item:
            count += 1
    return count
