def derivative(xs: list):
    return [i*coeff for i, coeff in enumerate(xs) if i > 0]