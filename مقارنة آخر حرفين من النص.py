from typing import List
def compare_two_words(s1: str, s2: str) -> bool:
	return s1[-1:-3:-1] == s2[-1:-3:-1]
