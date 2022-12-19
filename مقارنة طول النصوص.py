from typing import List
def str_len_comparison(words: List[str]) -> bool:
    if not words or len(words) < 2: return False
    return True if len(set([len(i) for i in words])) < 2 else False
