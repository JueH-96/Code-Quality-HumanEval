def multiply(a, b):
    """Take two integers and return the product of their unit digits."""
    return (abs(a) % 10) * (abs(b) % 10)