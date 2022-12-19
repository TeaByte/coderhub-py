from typing import List
def oddsVsEvens(num: int) -> str:
    even, odd = 0, 0
    for i in str(num):
        if int(i) % 2==0: even += int(i)
        else: odd += int(i)
    return 'even' if even>odd else ('equal' if even==odd else 'odd')
