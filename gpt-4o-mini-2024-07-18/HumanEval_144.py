def simplify(x, n):
    from fractions import Fraction
    
    # Convert string fractions to Fraction objects
    frac_x = Fraction(x)
    frac_n = Fraction(n)
    
    # Multiply the two fractions
    result = frac_x * frac_n
    
    # Check if the result is a whole number
    return result.denominator == 1