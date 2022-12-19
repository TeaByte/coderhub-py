from typing import List
def date_formating(date: str) -> str:
    date = date.split('-')
    return f'{date[-1]}-{date[1]}-{date[0]}'
