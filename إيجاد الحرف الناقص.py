from typing import List
def missingLetter(txt: str) -> str:
    abc = 'abcdefghijklmnopqrstuvwxyz'
    start = abc.index(txt[0])
    for i in range(len(txt)):
        if txt[i] != abc[start+i]: return abc[start+i]
    return 'No Missing Letter'
