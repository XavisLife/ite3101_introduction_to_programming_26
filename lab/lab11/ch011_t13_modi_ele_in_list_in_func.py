n = [3, 5, 7]

"""""
def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
""""


def double_list(x):
    new_list = []
    for item in x:
        new_list.append(item * 2)
    return new_list


print(double_list(n))
