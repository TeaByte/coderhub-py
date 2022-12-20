from typing import List
def similarOrdered(word1: str, word2: str) -> str:
    word1 = ''.join(sorted(list(dict.fromkeys(word1))))
    word2 = ''.join(sorted(list(dict.fromkeys(word2))))
    x = ''.join([j[0] if j[1] else ' ' for j in [(i, i in word2) for i in word1]])
    try: return sorted([i for i in x.split()])[0]
    except IndexError: return 'No matches found'
