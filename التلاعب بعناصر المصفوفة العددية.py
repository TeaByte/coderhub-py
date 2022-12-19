from typing import List
def filp_even_odd(numbers: List[int]) -> List[int]:
    return [i-1 if i%2 else i+1 for i in numbers]
