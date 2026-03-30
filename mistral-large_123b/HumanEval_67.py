def fruit_distribution(s, n):
    import re
    numbers = list(map(int, re.findall(r'\d+', s)))
    total_apples_oranges = sum(numbers)
    return n - total_apples_oranges