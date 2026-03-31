from typing import List, Tuple
import numpy as np

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if len(numbers) == 0:
        return (0, 1)
    
    sum = np.sum(np.array(numbers))
    product = np.prod(np.array(numbers))
    return (sum, product)