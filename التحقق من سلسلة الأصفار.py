from typing import List
def longestZero(strParam: str) -> str:
    return max([i for i in strParam.split('1') if i])