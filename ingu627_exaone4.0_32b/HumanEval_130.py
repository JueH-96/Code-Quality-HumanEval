def tri(n):
    if n < 0:
        return []
    sequence = []
    for i in range(n + 1):
        if i == 0:
            sequence.append(1)
        elif i == 1:
            sequence.append(3)
        else:
            if i % 2 == 0:
                term = 1 + i // 2
                sequence.append(term)
            else:
                # For odd i, we need tri(i-1) + tri(i-2) + tri(i+1)
                # But tri(i+1) might not be computed yet. However, i+1 is even, so it can be computed directly.
                term_i_plus_1 = 1 + (i + 1) // 2
                term = sequence[i - 2] + sequence[i - 1] + term_i_plus_1
                sequence.append(term)
    return sequence