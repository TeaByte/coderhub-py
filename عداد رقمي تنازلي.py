from typing import List
def countDown(number: int) -> str:
    return ' '.join([str(i) for i in range(number, -1, -1)])
