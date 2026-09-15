grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

total = 0
def grades_sum(scores: list) -> int:
    
    for score in scores:
        total += score
    return total


grades_sum(grades)
