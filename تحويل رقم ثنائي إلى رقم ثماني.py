from typing import List
def bin_to_oct(b: str) -> int:
    return int(oct(int(b, 2)).split('o')[1])
