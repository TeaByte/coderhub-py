from typing import List
def hashtag_it(my_array: List[str]) -> str:
    return ' '.join([f'#{i}' for i in my_array])
