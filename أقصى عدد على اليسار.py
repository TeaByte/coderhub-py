from typing import List
def left_digit(strParam: str) -> int:
    return int([i for i in strParam if i.isdigit()][0])
