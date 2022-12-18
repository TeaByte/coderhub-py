from typing import List
def sum_two_smallest_nums(arr: List[int]) -> int:
    first = min(arr)
    del arr[arr.index(first)]
    return first + min(arr)