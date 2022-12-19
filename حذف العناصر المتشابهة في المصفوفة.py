from typing import List
def remove_duplicate(arr: List[int]) -> List[int]:
    return list(dict.fromkeys(arr))
