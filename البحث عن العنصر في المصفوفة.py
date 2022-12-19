from typing import List
def search(word: str, character: str) -> int:
    for e, i in enumerate(word):
        if i == character: return e
    return -1
