from typing import List
def sum_even(arr: List[int]) -> int:
    return sum([i for i in arr if i%2==0])
