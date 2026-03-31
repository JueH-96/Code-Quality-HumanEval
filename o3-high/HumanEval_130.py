def tri(n):
    """Return a list with the first n + 1 numbers of the Tribonacci sequence as
    defined in the problem statement.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    seq = []
    for k in range(n + 1):
        if k == 0:                     # tri(0) = 1 (even rule)
            seq.append(1)
        elif k == 1:                   # tri(1) = 3 (given)
            seq.append(3)
        elif k % 2 == 0:               # even k ≥ 2
            seq.append(1 + k // 2)
        else:                          # odd k ≥ 3
            even_next = 1 + (k + 1) // 2   # tri(k + 1), with k + 1 even
            seq.append(seq[k - 1] + seq[k - 2] + even_next)
    return seq