def simplify(x, n):
    numerator_x, denominator_x = map(int, x.split('/'))
    numerator_n, denominator_n = map(int, n.split('/'))
    
    product_numerator = numerator_x * numerator_n 
    product_denominator = denominator_x * denominator_n 

    # Check if the product is a whole number
    return product_numerator % product_denominator == 0