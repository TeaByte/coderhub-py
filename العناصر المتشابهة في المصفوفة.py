from typing import List
def get_duplicate_elements(arr: List[int]) -> List[int]:
    return [i for i in list(dict.fromkeys(arr)) if arr.count(i) > 1]