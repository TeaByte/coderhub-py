from typing import List
def less_or_more_than_zero(number: int) -> str:
    return 'Greater than zero' if number>0 else ('Equal to zero' if not number else 'Less than zero')
