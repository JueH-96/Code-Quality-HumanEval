def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    from collections import Counter
    counts = Counter(l)
    for i in range(len(l)):
        counts[l[i]] -= 1
        for j in range(i+1, len(l)):
            counts[l[j]] -= 1
            needed = -(l[i] + l[j])
            if counts[needed] > 0:
                return True
            counts[l[j]] += 1
        counts[l[i]] += 1
    return False