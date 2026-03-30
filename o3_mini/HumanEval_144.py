def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    
    # Compute the product of the two fractions
    product_numerator = num1 * num2
    product_denominator = den1 * den2
    
    # Simplifying the fraction is extraneous; it's enough to check if product_numerator is 
    # divisible by product_denominator.
    return product_numerator % product_denominator == 0