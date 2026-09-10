from typing import List


n = [3, 5, 7]


def double_list(x: List[int]) -> List[int]:
    double_list = List[int]
    for i in range(0, len(x)):
        double_list.append(x[i] * 2)
    return double_list


print(double_list(n))
