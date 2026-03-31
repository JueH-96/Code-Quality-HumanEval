def poly_value(xs, x):
    """Evaluate the polynomial at x given coefficients xs."""
    return sum(coeff * (x ** i) for i, coeff in enumerate(xs))

def find_root(xs, max_iterations=100, tolerance=1e-9):
    """
    Find a real root of the polynomial defined by coefficients xs.
    
    Args:
        xs: List of polynomial coefficients, where xs[i] is the coefficient
            for x^i.
        max_iterations: Maximum number of iterations for convergence.
        tolerance: The acceptable error tolerance for the root approximation.
    
    Returns:
        float: Approximated real root of the polynomial.
        
    Raises:
        ValueError: If no sign change is found within the search range, indicating
                     no real root was found in the tested interval.
    """
    # Search for an interval with a sign change
    x = 0.0
    max_search = 100  # Maximum steps to find an initial interval
    f_x = poly_value(xs, x)
    
    # Check if x=0 is a root
    if abs(f_x) < tolerance:
        return x
    
    step = 1.0
    for _ in range(max_search):
        x += step
        current = poly_value(xs, x)
        previous = f_x
        
        if (current > 0 and previous < 0) or (current < 0 and previous > 0):
            # Sign change found; apply bisection method
            break
        else:
            # Prepare for next step
            f_x = current
            x += step  # Move further in the same direction
        
    else:
        # No sign change found within search steps
        raise ValueError("No real root found in the tested interval.")
    
    # Apply bisection method between x-step and x
    a = x - step
    b = x
    
    for _ in range(max_iterations):
        mid = (a + b) / 2
        f_mid = poly_value(xs, mid)
        
        if abs(f_mid) < tolerance:
            return mid
        
        # Update interval based on sign of function at midpoint
        if (f_mid > 0 and f_x < 0) or (f_mid < 0 and f_x > 0):
            b = mid
        else:
            a = mid
        
        # Check for convergence
        if abs(b - a) < tolerance:
            return (a + b) / 2
    
    # If max iterations reached without sufficient convergence
    return (a + b) / 2

# Example usage:
# For polynomial x^2 - 4, coefficients are [-4, 0, 1]
xs = [-4, 0, 1]
root = find_root(xs)
print(f"Found root at {root}")