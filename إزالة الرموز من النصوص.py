from typing import List
def removeSpecialCharacters(strParam: str) -> str:
    return ''.join([i for i in strParam if str(i).isalnum() or i in ['-', '_', ' ']])