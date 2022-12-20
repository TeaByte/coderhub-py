from typing import List
import re

def isEmail(email: str) -> bool:
    return True if re.search(r'^\w+[A-z-_.0-9]*@\w+\.\w{2,}', email) else False