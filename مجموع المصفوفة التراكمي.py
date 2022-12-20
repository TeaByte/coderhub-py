from typing import List
def cumulative_sum(arr: List[int]) -> List[int]:
    return [sum(arr[:i+1]) for i in range(len(arr))]