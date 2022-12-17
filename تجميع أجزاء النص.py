from typing import List
def isInterleave(A: str, B: str, C: str) -> bool:
    C, AB = list(C), list(A+B)
    for i in range(len(AB)):
        value = AB.pop()
        if value in C: del C[C.index(value)]
        else: return False
    return True
