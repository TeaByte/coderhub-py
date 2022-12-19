from typing import List
def calculate_sum(lst: List[int]) -> int:
    result = 0
    for i in lst:
        if i != 7: result += i
        else: break
    return result
        
