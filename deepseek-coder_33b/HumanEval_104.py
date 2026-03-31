def unique_digits(x):
    return sorted([num for num in x if all(int(i) % 2 != 0 for i in str(num))])