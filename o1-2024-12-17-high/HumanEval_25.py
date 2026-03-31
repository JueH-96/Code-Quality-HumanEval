from typing import List

def factorize(n: int) -> List[int]:
    result = []
    while n % 2 == 0:
        result.append(2)
        n //= 2
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            result.append(factor)
            n //= factor
        factor += 2
    if n > 1:
        result.append(n)
    return result