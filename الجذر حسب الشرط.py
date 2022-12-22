import math
from typing import List
def root_check(sqr: float, num: int) -> int:
    return int(math.sqrt(sqr)) if math.sqrt(sqr) == num else 0
