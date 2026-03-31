def is_product_integer(x_str, n_str):
    # Split each fraction into numerator and denominator
    x_parts = list(map(int, x_str.split('/')))
    if len(x_parts) != 2:
        return False
    num_x, den_x = x_parts[0], x_parts[1]
    
    n_parts = list(map(int, n_str.split('/')))
    if len(n_parts) != 2:
        return False
    num_n, den_n = n_parts[0], n_parts[1]
    
    # Calculate the product's numerator and denominator
    p_num = num_x * num_n
    p_den = den_x * den_n
    
    # Check for division by zero (though problem likely assumes non-zero denominators)
    if p_den == 0:
        return False
    
    # Determine if the product is an integer
    return (p_num % p_den) == 0