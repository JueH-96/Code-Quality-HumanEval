def generate_sequence(n):
    sequence = []
    for k in range(n):
        if k % 2 == 0:
            # Even index: (k/2)^2 +1
            term = (k // 2) ** 2 + 1
        else:
            # Odd index: ((k//2)+1)*((k//2)+3)
            m = k // 2
            term = (m + 1) * (m + 3)
        sequence.append(term)
    return sequence

# Example usage:
n = 5  # To generate terms for indices 0 to 4
print(generate_sequence(n))  # Output: [1, 3, 2, 8, 5]