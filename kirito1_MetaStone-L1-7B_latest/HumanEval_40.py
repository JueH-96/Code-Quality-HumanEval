import itertools

def triples_sum_to_zero(l: list):
    if len(l) < 3:
        return False
    for triplet in itertools.combinations(l, 3):
        if sum(triplet) == 0:
            return True
    return False