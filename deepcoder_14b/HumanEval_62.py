def derivative(xs):
    if len(xs) < 2:
        return []
    return [(j + 1) * xs[j + 1] for j in range(len(xs) - 1)]