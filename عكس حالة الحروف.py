from typing import List
def reverse_case(strParam: str) -> str:
    result = ''
    for i in strParam:
        if i.isalpha():
            if i.isupper(): result += i.lower()
            else: result += i.upper()
        else: result += i
    return result
                
