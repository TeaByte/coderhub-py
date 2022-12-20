from typing import List
def sortByLength(txt: str) -> str:
    return ' '.join([j[1] for j in sorted([(len(i), i) for i in txt.split()])])
