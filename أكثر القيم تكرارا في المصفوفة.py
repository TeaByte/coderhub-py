from typing import List
def most_frequent_element(arr: List[int]) -> int:
    x = [arr.count(i) for i in arr]
    return arr[x.index(max(x))]
