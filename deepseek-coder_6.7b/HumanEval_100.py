def make_a_pile(n):
    pile = []
    
    for i in range(1, n + 1):
        if i % 2 == 0: # if even level
            stones = 2 * i - 1
            pile.append(stones)
        else: # if odd level
            stones = 2 * i
            pile.append(stones)
    
    return pile