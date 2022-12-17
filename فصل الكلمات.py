from typing import List
def cap_space(txt: str) -> str:
    result = ''
    for i in txt:
        if i.isupper(): result += f' {i.lower()}'
        else: result += i
    return result