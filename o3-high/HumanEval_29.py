from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings, returning only those that start with a given prefix.

    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    if not prefix:
        # If the prefix is empty, every string matches.
        return list(strings)
    return [s for s in strings if s.startswith(prefix)]