def make_a_pile(n):
    pile = [n]
    step = 2 if n % 2 == 0 else 2
    for _ in range(1, n):
        current = pile[-1] + step
        pile.append(current)
    return pile