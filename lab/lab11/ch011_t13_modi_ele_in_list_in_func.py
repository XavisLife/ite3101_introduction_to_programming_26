from typing import List


n = [3, 5, 7]


def double_list(x: List[int]) -> List[int]:
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x[i]


print(double_list(n))
