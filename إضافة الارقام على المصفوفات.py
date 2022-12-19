from typing import List
def add_five(arr: List[str]) -> List[str]:
        if not arr: return arr
        return [f'{i}5' for i in arr]
