n = [3, 5, 7]


def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x


# problematic.. Didn't the requirement mentioned return with the exist list instead of new list?
double_list(n)
print(double_list(n))
