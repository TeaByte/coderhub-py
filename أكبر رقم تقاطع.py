from typing import List
def getBiggestShared(a: List[int], b: List[int]) -> int:
        x = max(a)
        while True:
            if x in b: return x
            else: 
                del a[a.index(x)]
                x = max(a)
