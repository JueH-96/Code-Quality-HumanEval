def fruit_distribution(s, n):
    parts = s.split(' and ')
    apple_str = int(parts[0].split()[0])
    orange_str = int(parts[1].split()[0])
    return n - (apple_str + orange_str)