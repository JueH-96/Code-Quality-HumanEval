import re

def fix_spaces(text):
    def replacer(match):
        length = match.group().count(' ')
        if length == 1:
            return '_'
        elif length >= 3:
            return '-'
        else:  # length is exactly 2
            return '__'
    
    return re.sub(r'\s+', replacer, text)