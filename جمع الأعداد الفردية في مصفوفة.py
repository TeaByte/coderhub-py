from typing import List
def sumOdd(arr: List[int]) -> int:
    return sum([i for i in arr if i%2 != 0])