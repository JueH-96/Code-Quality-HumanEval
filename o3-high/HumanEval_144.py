import math

def simplify(x, n):
    """Return True if the product of the two fraction strings x and n is
    a whole number, otherwise False."""
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))

    # Cross-cancel common factors to keep the numbers small
    g = math.gcd(num1, den2)
    num1 //= g
    den2 //= g

    g = math.gcd(num2, den1)
    num2 //= g
    den1 //= g

    # After cancellation, check if the denominator divides the numerator
    return (num1 * num2) % (den1 * den2) == 0