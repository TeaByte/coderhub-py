from typing import List
def Decimal_places(num: str) -> int:
    return len(num.split('.')[1]) if '.' in num else 0
