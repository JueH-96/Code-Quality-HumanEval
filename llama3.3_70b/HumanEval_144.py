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
    # Split the input strings into numerators and denominators
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    # Calculate the product of the two fractions
    product_num = x_num * n_num
    product_denom = x_denom * n_denom

    # Check if the product is a whole number by checking if the denominator can divide the numerator
    return product_num % product_denom == 0 or product_denom % product_num == 0 and product_num != 0