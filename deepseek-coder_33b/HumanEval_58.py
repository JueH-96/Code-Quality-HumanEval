def common(l1: list, l2: list) -> list:
    return sorted(list(set(l1) & set(l2)))