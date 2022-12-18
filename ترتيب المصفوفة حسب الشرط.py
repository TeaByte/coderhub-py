from typing import List
def sort_array(my_array: List[int], typeParam: str) -> List[int]:
    return sorted(my_array) if typeParam == 'S' else sorted(my_array, reverse=True)