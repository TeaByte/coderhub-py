from typing import List
def namesSort(namesArray: List[str], order: str) -> List[str]:
    return [j[1] for j in sorted([(len(i), i) for i in namesArray], reverse=(True if order=='DESC' else False))]
