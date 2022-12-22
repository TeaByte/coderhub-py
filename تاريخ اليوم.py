from typing import List
def date_format(date: str) -> str:
    x = date.split('/')
    return f'{date} | {date.replace("/", "-")} | {x[1]}/{x[2]}/{x[0]}'
