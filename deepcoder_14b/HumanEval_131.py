def digits_product(n):
    product = 1
    has_odds = False
    for c in str(n):
        d = int(c)
        if d % 2 != 0:
            product *= d
            has_odds = True
    return product if has_odds else 0