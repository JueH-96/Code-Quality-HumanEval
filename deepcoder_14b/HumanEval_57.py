def monotonic(l: list) -> bool:
    if len(l) <= 1:
        return True
    increasing = all(x <= y for x, y in zip(l, l[1:]))
    decreasing = all(x >= y for x, y in zip(l, l[1:]))
    return increasing or decreasing