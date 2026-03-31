from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    count = Counter(numbers)
    return [n for n in numbers if count[n] == 1]