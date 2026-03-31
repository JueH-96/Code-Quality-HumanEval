from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    if not strings:
        return None

    longest_str = strings[0]
    max_len = len(longest_str)

    for s in strings[1:]:
        current_len = len(s)
        if current_len > max_len:
            longest_str = s
            max_len = current_len

    return longest_str