def derivative(xs: list):
    result = []
    for i in range(1, len(xs)):
        result.append(i * xs[i])
    return result