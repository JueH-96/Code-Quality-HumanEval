def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = [0] * 3  # to store the count of elements with remainder 0, 1 and 2 when divided by 3

    for num in a:
        count[num % 3] += 1

    total_triples = (count[0] * (count[0] - 1) * (count[0] - 2) // 6) + \
                     (count[1] * (count[1] - 1) // 2) * count[0] + \
                     (count[2] * (count[2] - 1) // 2) * count[0]
    return total_triples