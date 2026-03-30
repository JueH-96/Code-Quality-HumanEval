def unique_digits(x):
    def has_even_digit(n):
        return any(int(digit) % 2 == 0 for digit in str(n))

    return sorted([num for num in x if not has_even_digit(num)])