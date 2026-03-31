from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    max_len = len(max(strings, key=len))  # Find the maximum length of all strings in list
    for string in strings:  # Iterate through each string
        if len(string) == max_len:  # If string's length is same as maximum length
            return string  # Return that string as it is longest