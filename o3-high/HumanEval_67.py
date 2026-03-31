def fruit_distribution(s, n):
    """
    Given a string describing the number of apples and oranges in a basket and
    the total number of fruits in that basket, return the number of mangoes.
    """
    import re
    total_known = sum(map(int, re.findall(r'\d+', s)))
    return n - total_known