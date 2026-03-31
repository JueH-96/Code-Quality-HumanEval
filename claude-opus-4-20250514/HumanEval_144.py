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
    # Parse the fractions
    x_parts = x.split('/')
    x_num, x_den = int(x_parts[0]), int(x_parts[1])
    
    n_parts = n.split('/')
    n_num, n_den = int(n_parts[0]), int(n_parts[1])
    
    # Multiply the fractions: (a/b) * (c/d) = (a*c)/(b*d)
    result_num = x_num * n_num
    result_den = x_den * n_den
    
    # Check if the result is a whole number
    return result_num % result_den == 0