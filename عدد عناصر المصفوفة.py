from typing import List
def num_elements(my_array: List[int]) -> int:
    count = 0
    for i in my_array: count += 1
    return count
