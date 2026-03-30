def fruit_distribution(s, n):
    import re
    numbers = list(map(int, re.findall(r'\d+', s)))
    if len(numbers) >= 2:
        apples, oranges = numbers[0], numbers[1]
        return n - apples - oranges
    else:
        return None