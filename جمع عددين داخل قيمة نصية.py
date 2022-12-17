from typing import List
def addStrNums(num1: str, num2: str) -> str:
    try: return str( int(num1) + int(num2) )
    except: return "-1"