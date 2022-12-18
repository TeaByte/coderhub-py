from typing import List
def input_type(value: str) -> str:
    return 'string' if value[0].isalpha() else ('double' if value[0].isdigit() and '.' in value else 'integer')
