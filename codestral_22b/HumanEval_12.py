from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    else:
        max_len = max(len(string) for string in strings)
        longest_strings = [string for string in strings if len(string) == max_len]
        return longest_strings[0]