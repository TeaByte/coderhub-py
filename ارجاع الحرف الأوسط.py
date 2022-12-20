from typing import List
def middle_char(word: str) -> str:
    	mid = int(len(word)/2)
    	return word[mid if len(word)%2 else mid-1:mid+1]
