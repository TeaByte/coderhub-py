from typing import List
def operation(num1: int, num2: int) -> str:
        if num1+num2==24: return "added"
        if num1-num2==24 or num2-num1==24: return "subtracted"
        if num1/num2==24 or num2/num1==24: return "divided"
        if num1*num2==24: return "multiplied"
        return "None"
