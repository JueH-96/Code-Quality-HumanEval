def derivative(p):
    if not p:
        return []
    return [p[i] * i for i in range(1, len(p))]