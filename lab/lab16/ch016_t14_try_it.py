squares = [x * x for x in range(1, 10)]
print(list(filter(lambda x: x >= 30 and x <= 70, squares)))
