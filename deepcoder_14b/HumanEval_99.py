import math

def round_half_up(x):
    n = math.floor(x)
    m = n + 1
    distance_n = abs(x - n)
    distance_m = abs(m - x)
    if distance_n < distance_m:
        return int(n)
    elif distance_m < distance_n:
        return int(m)
    else:  # Tie case, round up by returning m
        return int(m)

# Example usage:
print(round_half_up(2.5))      # Output: 3
print(round_half_up(-2.5))     # Output: -2
print(round_half_up(14.5))     # Output: 15
print(round_half_up(-14.5))    # Output: -14
print(round_half_up(2.4))      # Output: 2
print(round_half_up(2.6))      # Output: 3
print(round_half_up(-2.4))     # Output: -2