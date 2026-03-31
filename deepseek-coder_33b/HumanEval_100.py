def make_a_pile(n):
    pile = []
    for i in range(1, n+1):
        if n % 2 == 0:
            pile.append(n + 2*i - 1)
        else:
            pile.append(n + 2*i)
    return pile