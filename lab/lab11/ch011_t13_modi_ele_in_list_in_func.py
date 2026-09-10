from typing import List


n = [3, 5, 7]


def double_list(x: List[int]) -> List[int]:
    y = [int]
    for i in range(0, len(x)):
        y[i] = x[i] * 2
    return y
# Don't forget to return your new list!


print(double_list(n))
