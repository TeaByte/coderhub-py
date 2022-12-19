from typing import List
def arrowDuplicates(word: str) -> str:
    word = word.lower()
    return ''.join(['<' if word.count(i) > 1 else '>' for i in word])
