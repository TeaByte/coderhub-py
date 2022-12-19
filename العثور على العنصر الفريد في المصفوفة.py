from typing import List
def unique(arr: List[int]) -> List[int]:
    return [i for i in arr if arr.count(i) < 2]
