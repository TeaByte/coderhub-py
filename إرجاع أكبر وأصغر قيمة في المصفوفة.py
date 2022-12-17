from typing import List
def largest_smallest(array_values: List[int]) -> List[int]:
    #return [max(array_values), min(array_values)] for noobs
    _max, _min = array_values[0], array_values[0]
    for i in array_values:
        if i > _max: _max = i
        elif i < _min: _min = i
    return [_max, _min]