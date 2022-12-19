from typing import List
def first_n_vowels(phrase: str, n: int) -> str:
    x = ''.join([i for i in phrase if i in "aeiouAEIOU"][:n+1])
    try: y = [x[j] for j in range(n)]
    except: return 'invalid'
    else: return ''.join(y)
