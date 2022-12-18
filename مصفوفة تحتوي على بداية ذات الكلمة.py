from typing import List
def find_prefix(words: List[str], text: str) -> List[str]:
    x = [i for i in words if text.lower() in i.lower()]
    return x if x else ['No matches found']