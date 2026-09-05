
from typing import List


def median(lst: List[int]) -> float:
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    if length % 2 == 0
        index_1 = length // 2 - 1
        index_2 = length // 2
        m = (sorted_lst[index_1] + sorted_lst[index_2]) / 2.0
        return m
    else:
        index = len(sorted_lst) // 2
        return sorted_lst[index]
