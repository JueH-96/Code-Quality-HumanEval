from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    
    max_str = strings[0]
    max_len = len(max_str)
    
    for s in strings[1:]:
        current_len = len(s)
        if current_len > max_len:
            max_str = s
            max_len = current_len
    
    return max_str