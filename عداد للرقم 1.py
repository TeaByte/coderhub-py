from typing import List
def count_ones(num: int) -> int:
    result = []
    while(num):
        if num%2: result.append(1)
        num = int(num/2)
    return len(result)