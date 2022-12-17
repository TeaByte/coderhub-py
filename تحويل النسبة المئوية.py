from typing import List
def convertPercent(percentage: str) -> float:
    return float(''.join([i for i in percentage if i.isdigit()]))/100