from typing import List
def stringCheck(value: List[str]) -> bool:
    return True if len(set(value)) < 2 else False