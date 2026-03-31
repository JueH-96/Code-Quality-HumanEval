def simplify(x, n):
    # Parse the fractions x and n into numerators and denominators
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    # Calculate the product's numerator and denominator
    numerator_product = x_num * n_num
    denominator_product = x_den * n_den
    
    # Check if the product is a whole number (denominator divides numerator without remainder)
    return numerator_product % denominator_product == 0