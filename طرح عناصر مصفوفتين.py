from typing import List
def sub_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    return [arr2[i] - arr1[i]  for i in range(len(arr1))]
