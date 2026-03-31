from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    s = sum(numbers) if numbers else 0
    p = math.prod(numbers) if numbers and len(numbers) > 1 else 1
    return (s, p)